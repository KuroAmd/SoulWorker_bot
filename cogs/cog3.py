import discord
from discord.ext import commands
#import datetime
import random
import string
import requests

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events

    #Cmds
## Retype the sentense
    @commands.hybrid_command(aliases=["كلمه","كلمة","اسرع", "کلمه"])
    async def words(self, ctx, t:int = 7):
        print(t, " seconds to type ")
        word=random.choice(open("Ar_words.txt","r").read().split('\n'))
        print(word)
        em = discord.Embed(title=word, colour= discord.Colour.gold())
        bmsg = await ctx.send(embed= em)
        await ctx.send(f"اكتب خلال {t} ثوان")
        await bmsg.delete(delay= t)
        msg= await self.client.wait_for('message',timeout = t)
        print(msg.content)
        print(bmsg)
        if msg.content == word:
          await msg.reply('احسنت')
        else:
          await msg.reply('اخطأت')

## Cross & Nots
    @commands.command(aliases=['xno',"اکس"])
    async def tictac(self,ctx, player_2:discord.Member, sym_1="✖️",sym_2="⭕"):
        if player_2.bot:
            await ctx.send("Can't play with a bot")
            if ctx.author.id!=444806806682730496:
              return
        player_1 = ctx.author
        print(player_1, player_2)
        #play = 1
        board = "```  1  |  2️  |  3️  \n-----|-----|-----\n  4️  |  5️  |  6️  \n-----|-----|-----\n  7️  |  8️  |  9️  ```"
        bmsg=await ctx.send(board)
        reactions = ('1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣')
        R = {'1️⃣':1,'2️⃣':2,'3️⃣':3,'4️⃣':4,'5️⃣':5,'6️⃣':6,'7️⃣':7,'8️⃣':8,'9️⃣':9}

        for n in reactions:
            await bmsg.add_reaction(n)

        for i in range(9):
            print("turn" , i)
            def ch(reaction, user):
                if i%2 != 1:
                    print("1st player's turn")
                    turn = player_1
                else:
                    print("2nd player's turn")
                    turn = player_2
                print(reaction)
                print(user)
                return user==turn and str(reaction.emoji) in reactions
            react= await self.client.wait_for('reaction_add',check=ch)
            #print(f"here we have {react[1].user}")
            print(f"and this is {react[0].emoji}")
            p = R.get(react[0].emoji)
            if i%2 == 1:
                board= board.replace(str(p),f"{str(sym_2)}")
            else:
                board= board.replace(str(p),f"{str(sym_1)}")
            await bmsg.edit(content=board)
            try:
              await bmsg.clear_reaction(react[0].emoji)
            except Exception as e:
              print(e)
              await ctx.send('btw, failed to remove reaction')


## Hangman
    @commands.hybrid_command(aliases=["المشنقة","الجلاد"]) # how about make it edit the 1st msgs every letter
    async def hangman(self,ctx):
        """You've 5 tries to guess a letters of a random word (please send 1 letter at a time)""" # # word count in english2.txt is 65194 words!
        word=random.choice(open("english2.txt","r").read().split())
        #region initialization
        win = False
        strikes = [] # can do win=False if strikes==5
        guesses = []
        display_word = len(word)*['- '] 
        print("\nLet's play HANGMAN!\n")
        print(word,"\n",display_word,'\n')
        await ctx.send("Let's play HANGMAN! Can you guess in 5 strikes?")
        await ctx.send(content=("".join(display_word)+"\n."))
        #endregion
        #region game loop
        while (win == False) and (len(strikes) < 5):
          #  letter = raw_input("Guess a letter! ").lower()
          #  define bmsg
            def ch(message):
              return message.author.bot==False
            msg= await self.client.wait_for('message',check=ch)
            #print(msg)
            letter=msg.content.lower()
            print(letter)
            await ctx.typing()

            if not letter in string.ascii_lowercase or letter=='':
                #await ctx.send("not a valid guess, please try again")
                continue

            if letter in guesses:
                await msg.reply('You already guessed that one, please try again.')
            else:
                guesses += [letter]
                if letter in word:
                    print("\nCorrect Guess!",letter)
                    await msg.reply(f"Yes!   **{letter}**")
                    for x in range(0, len(word)):
                        if letter == word[x]:
                          display_word[x] = word[x]
                else:
                    strikes += [letter]
                    print("\nIncorrect Guess.")
                    await msg.reply("wrong guess...")

            await ctx.send(embed=discord.Embed(title="The mystery word so far:",description= "".join(display_word)))
            await ctx.send(("Already guessed letters: ", guesses))
            await ctx.send(("Strikes remaining: " + str(5-len(strikes)))) #send pic of hangman
            if display_word == list(word):
                win = True
            #print(win)
        #endregion

        if win == True:
            await msg.reply("Hats off to you! You win!")
        else:
            hang="```\n\t|\n\to\n  --|--\n   /\```"
            await msg.reply(f"Better luck time!\nCan't win 'em all.\n{hang}")
        print("The word was '", ''.join(word) , "'")
        await ctx.send("The word is '"+''.join(word)+"'")

        #await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


    @commands.hybrid_command(aliases=["chb","chat",'محادثة']) ## am getting 403 (Forbidden) response :/
    async def chatbot(self, ctx, msg:str):
      
        #making a GET request to the endpoint.
        resp = requests.get("https://some-random-api.com/chatbot?message={0}".format(msg))
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        print(content)
        bmsg = await ctx.reply(content)
        await bmsg.add_reaction(self.client.emojis[0])
        

async def setup(client):
    await client.add_cog(Games(client))