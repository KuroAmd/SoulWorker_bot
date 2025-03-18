import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio as fpcm
#from discord.voice_client import VoiceClient
from yt_dlp import YoutubeDL as ytdl
import asyncio
from datetime import datetime, timezone
import aiohttp
#import json
#import re
import os
from discord import app_commands
from discord.ext.music import MusicClient, WAVAudio, Track
#import ffmpeg
import ctypes.util
#import opus
import sys

#ydl_opts = {
# 'usenetrc': opts.usenetrc,
# 'username': opts.username,
# 'password': opts.password,
# 'twofactor': opts.twofactor,
# 'videopassword': opts.videopassword,
# 'ap_mso': opts.ap_mso,
# 'ap_username': opts.ap_username,
#  'ap_password': opts.ap_password,
#  'quiet': (opts.quiet or any_getting or any_printing),
#  'no_warnings': opts.no_warnings,
#  'forceurl': opts.geturl,
#  'forcetitle': opts.gettitle,
#  'forceid': opts.getid,
#  'forcethumbnail': opts.getthumbnail,
#  'forcedescription': opts.getdescription,
#  'forceduration': opts.getduration,
#  'forcefilename': opts.getfilename,
#  'forceformat': opts.getformat,
#  'forcejson': opts.dumpjson or opts.print_json,
#  'dump_single_json': opts.dump_single_json,
#  'simulate': opts.simulate or any_getting,
#  'skip_download': opts.skip_download,
#  'format': opts.format,
#  'listformats': opts.listformats,
#  'outtmpl': outtmpl,
#  'outtmpl_na_placeholder': opts.outtmpl_na_placeholder,
#  'autonumber_size': opts.autonumber_size,
#  'autonumber_start': opts.autonumber_start,
#  'restrictfilenames': opts.restrictfilenames,
#  'ignoreerrors': opts.ignoreerrors,
#  'force_generic_extractor': opts.force_generic_extractor,
#  'ratelimit': opts.ratelimit,
#  'nooverwrites': opts.nooverwrites,
#  'retries': opts.retries,
#  'fragment_retries': opts.fragment_retries,
#  'skip_unavailable_fragments': opts.skip_unavailable_fragments,
#  'keep_fragments': opts.keep_fragments,
#  'buffersize': opts.buffersize,
#  'noresizebuffer': opts.noresizebuffer,
#  'http_chunk_size': opts.http_chunk_size,
#  'continuedl': opts.continue_dl,
#  'noprogress': opts.noprogress,
#  'progress_with_newline': opts.progress_with_newline,
#  'playliststart': opts.playliststart,
#  'playlistend': opts.playlistend,
#  'playlistreverse': opts.playlist_reverse,
#  'playlistrandom': opts.playlist_random,
#  'noplaylist': opts.noplaylist,
#  'logtostderr': opts.outtmpl == '-',
#  'consoletitle': opts.consoletitle,
#  'nopart': opts.nopart,
#  'updatetime': opts.updatetime, # # want that!
#  'writedescription': opts.writedescription,
#  'writeannotations': opts.writeannotations,
#  'writeinfojson': opts.writeinfojson,
#  'writethumbnail': opts.writethumbnail,
#  'write_all_thumbnails': opts.write_all_thumbnails,
#  'writesubtitles': opts.writesubtitles,
#  'writeautomaticsub': opts.writeautomaticsub,
#  'allsubtitles': opts.allsubtitles,
#  'listsubtitles': opts.listsubtitles,
#  'subtitlesformat': opts.subtitlesformat,
#  'subtitleslangs': opts.subtitleslangs,
#  'matchtitle': decodeOption(opts.matchtitle),
#  'rejecttitle': decodeOption(opts.rejecttitle),
#  'max_downloads': opts.max_downloads,
#  'prefer_free_formats': opts.prefer_free_formats,
#  'verbose': opts.verbose,
#  'dump_intermediate_pages': opts.dump_intermediate_pages,
#  'write_pages': opts.write_pages,
#  'test': opts.test,
#  'keepvideo': opts.keepvideo,
#  'min_filesize': opts.min_filesize,
#  'max_filesize': opts.max_filesize, # # nice info
#  'min_views': opts.min_views,
#  'max_views': opts.max_views,
#  'daterange': date,
#  'cachedir': opts.cachedir,
#  'youtube_print_sig_code': opts.youtube_print_sig_code,
#  'age_limit': opts.age_limit,
#  'download_archive': download_archive_fn,
#  'cookiefile': opts.cookiefile,
#  'nocheckcertificate': opts.no_check_certificate,
#  'prefer_insecure': opts.prefer_insecure,
#  'proxy': opts.proxy,
#  'socket_timeout': opts.socket_timeout,
#  'bidi_workaround': opts.bidi_workaround,
#  'debug_printtraffic': opts.debug_printtraffic,
#  'prefer_ffmpeg': opts.prefer_ffmpeg,
#  'include_ads': opts.include_ads,
#  'default_search': opts.default_search, # # is that search?
#  'youtube_include_dash_manifest': opts.youtube_include_dash_manifest,
#  'encoding': opts.encoding,
#  'extract_flat': opts.extract_flat,
#  'mark_watched': opts.mark_watched,
#  'merge_output_format': opts.merge_output_format,
#  'postprocessors': postprocessors,
#  'fixup': opts.fixup,
#  'source_address': opts.source_address,
#  'call_home': opts.call_home,
#  'sleep_interval': opts.sleep_interval,
#  'max_sleep_interval': opts.max_sleep_interval,
#  'external_downloader': opts.external_downloader,
#  'list_thumbnails': opts.list_thumbnails,
#  'playlist_items': opts.playlist_items,
#  'xattr_set_filesize': opts.xattr_set_filesize,
#  'match_filter': match_filter,
#  'no_color': opts.no_color,
#  'ffmpeg_location': opts.ffmpeg_location,
#  'hls_prefer_native': opts.hls_prefer_native,
#  'hls_use_mpegts': opts.hls_use_mpegts,
#  'external_downloader_args': external_downloader_args,
#  'postprocessor_args': postprocessor_args,
#  'cn_verification_proxy': opts.cn_verification_proxy,
#  'geo_verification_proxy': opts.geo_verification_proxy,
#  'config_location': opts.config_location,
#  'geo_bypass': opts.geo_bypass,
#  'geo_bypass_country': opts.geo_bypass_country,
#  'geo_bypass_ip_block': opts.geo_bypass_ip_block,
# # just for deprecation check
#  'autonumber': opts.autonumber if opts.autonumber is True else None,
#  'usetitle': opts.usetitle if opts.usetitle is True else None
# }

#from youtube_dl import YoutubeDL

Q = asyncio.Queue()
mypl = []
somerandapi = "https://some-random-api.com"

gid = discord.Object(id=727092352363135077)


def load_s(mypl=mypl):
    for song in os.listdir("./songs/"):
        mypl += ["./songs/" + song]


def N_song(error=None):
    Q.put_nowait(mypl.pop(0))  # try... Nope next not playing


def q_n(error=None):
    #return print('done?\n')
    Q.get_nowait()


#loop1=False
import requests


def yt_search(arg):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'skipdownload' : 'True'}
    with ytdl(YDL_OPTIONS) as ydl:
        try:
            requests.get(arg)
        except:
            video = ydl.extract_info(
                f"ytsearch:{arg}", download=False)
            if video and 'entries' in video:
                video = video['entries'][0]  # takes the first element from the entries

        else:
            video = ydl.extract_info(arg, download=False)
    return video


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    # YouTube

    @commands.hybrid_command(aliases=['YT', 'yts', 'Youtube', "یوتیوب"])
    @app_commands.guilds()
    async def yt(self, ctx, *, arg):
        '''Search a YT vid'''
        await ctx.typing()
        print(arg)
        vid = yt_search(arg)
        if vid:
            s = vid['webpage_url']
            print("the url:\n" + s)
        else:
            s = "Video not found"
            print("Error 404 " ,s)
        await ctx.send(s)


    ## Doesn't work!
    @commands.command(hidden=True)
    async def Play(self, ctx, *, arg=None):
        '''testing discord.ext.music funcs (doesnt seem to work, and their docs succ)'''

        if mypl == []:
            load_s(mypl)
        song = mypl[0]
        print(song)
        try:
            song_n = song.replace("./songs/", "")
        except:
            song_n = song
        print(song_n)

        try:
            Vch = ctx.author.voice.channel
            mcl = await Vch.connect(cls= MusicClient)
            print("connected to {0}!".format(Vch))

            try:
              track = Track(
                  WAVAudio(song), # AudioSource
                  song,
                  url=arg if arg else "") # name
              print("find audio")

              await mcl.play(track)
              print("play audio")

            except Exception as e:
              print(e)

        except Exception as e:
          print(e)



    @commands.hybrid_command(aliases=['m', 'M', "موسيق", "موزیک"])
    @app_commands.guilds()
    async def music(self, ctx, arg: str = 'a', *, link=None):
        '''<join, play, stop, pause/resume , skip ,(search, playlist/queue and next are not yet working)> [link]'''

        if arg.lower() in ("join", "j", "connect"):  ## Connects to VC
            if link:  ## connect to vc if given name
                print(link)
                Vch = get(ctx.guild.voice_channels, name=link)
                if not Vch:
                    await ctx.send(f"VC '{link}' not found :/")
                    return
                await Vch.connect()
                bmsg = await ctx.send("Connected to {0}".format(Vch))
                await bmsg.delete(delay=5)
            elif ctx.author.voice:
                if ctx.guild.voice_client:
                    ctx.guild.voice_client.disconnect()
                Vch = ctx.author.voice.channel
                await Vch.connect()
                bmsg = await ctx.send(f"Connected to {Vch}")
                await bmsg.delete(delay=5)
            elif (not ctx.author.voice):
                Vch = get(ctx.guild.voice_channels, name="General")
                await Vch.connect()
                bmsg = await ctx.send("connected to General VC")
                await bmsg.delete(delay=5)
            else:
                bmsg = await ctx.send("You aren't in VC")
                await bmsg.delete(delay=5)
                print(ctx.guild.voice_channels)

        elif arg.lower() in ("search", "find", "f", "بحث"):
            """Incomplete"""
            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
            with ytdl(YDL_OPTIONS) as ydl:
                try:
                    requests.get(str(link))
                except Exception as e:
                    print(f"Error fetching link: {e}")
                    vid = ydl.extract_info(f"ytsearch:{link}", download=False)
                    if vid is None:
                        await ctx.send("Video not found")
                    elif 'entries' in vid:
                        vid = vid['entries'][0]  # take the first element from the entries
                else:
                    vid = ydl.extract_info(link, download=False)
                    if vid is None:
                        await ctx.send("Video not found")
                        return
                    elif 'entries' in vid:
                        vid = vid['entries'][0]  # take the first element from the entries
                    else:
                        # Handle single video case
                        print(vid) 
                        # ... Process the video info as needed
                    print(vid)
                    if 'entries' in vid:
                        songt = [entry['title'] for entry in vid['entries']]
                    else:
                        songt = [vid['title']] 
                    songt = "\n".join(songt)
                    await ctx.send(songt)
            pass
            ## give results and lets choose which one to play

        elif arg.lower() in ("play", "p", "شغل"):  ## in my pl, a way to play next is stop & play again

            if link == "opus":
                print("ctypes - Find opus:")
                a = ctypes.util.find_library('opus')
                print(a)

                print("Discord - Load Opus:")
                b = discord.opus.load_opus(a) if a else "Opus not found"
                print(b)

                print("Discord - Is loaded:")
                c = discord.opus.is_loaded()
                print(c)

            if not ctx.guild.voice_client:
                if ctx.author.voice:
                    Vch = ctx.author.voice.channel
                    await Vch.connect()
                    bmsg = await ctx.send(f"Connected to {Vch}")
                    await bmsg.delete(delay=5)
                elif not ctx.author.voice:
                    Vch = get(ctx.guild.voice_channels, name="General")
                    await Vch.connect()
                    bmsg = await ctx.send("connected to General VC")
                    await bmsg.delete(delay=5)
                else:
                    bmsg = await ctx.send("You aren't in VC")
                    await bmsg.delete(delay=7)
                    print(ctx.guild.voice_channels)
                    return
            if (len(ctx.guild.voice_client.channel.members) < 2):
                print("lonely...")
                await ctx.send("Waiting for someone else to join first")
                return
            if not ctx.guild.voice_client.is_playing():
                #song= None
                if not link:  ## Plays my Playlist
                    #  if not song:
                    #Q=mypl
                    print(Q)
                    if mypl == []:
                        load_s(mypl)
                    song = mypl[0]
                    print(song)
                    try:
                        song_n = song.replace("./songs/", "")
                    except:
                        song_n = song
                    print(song_n)
                    Vch = ctx.guild.voice_client
                    Vch.play(fpcm(song), after=Q.put_nowait(mypl.pop(0)))
                    #Vch.source= discord.PCMVolumeTransformer(Vch.source)
                    bmsg = await ctx.send(f"playing {song_n}")
                    await bmsg.delete(delay=5)

                else:
                    print(link)
                    ydl_opts = ytdl({
                        "quiet":
                        True,
                        "verbose":
                        True,
                        "format":
                        "bestaudio/best",
                        "ignoreerrors":
                        True,
                        "youtube_include_dash_manifest":
                        False,
                        "noplaylist":
                        True,
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                        'restrictfilenames':
                        True,
                        'nocheckcertificate':
                        True,
                        'logtostderr':
                        False,
                        'no_warnings':
                        True,
                        'default_search':
                        'auto',
                        'source_address':
                        '0.0.0.0'
                    })
                    bmsg = await ctx.send('Preparing song... Please wait.')
                    ul = yt_search(link)
                    if ul:
                        print(ul['title'])
                        print("url of vid:\n", ul['webpage_url'])
                    else:
                        print("Error: vid url not found")
                        return

                    Vch = get(self.client.voice_clients, guild=ctx.guild)

                    FFMPEG_OPTIONS = {
                        'before_options':
                        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                        'options': '-vn'
                    }

                    if not Vch.is_playing():
                        info = ydl_opts.extract_info(url=ul['webpage_url'],
                                                     download=False)
                        URL = info['formats'][0]['url'] if info else ''
                        print("URL to play:\n" + URL)
                        Vch.play(fpcm(URL, **FFMPEG_OPTIONS), after=q_n, stderr=sys.stderr)
                        await bmsg.delete()
                        bmsg = await ctx.send(f"Now playing\n> {ul['title']}")
                        Vch.is_playing()
                    #else:
                    #  await ctx.send("Already playing song")
                    #  return
            else:
                #add to Queue
                Q.put_nowait(link)
                #
                bmsg = await ctx.send('added to queue')
                await bmsg.delete(delay=3)

        elif arg.lower() in ("next", "skip"):  ## Should play next song in queue (incomplete)
            pq = Q.put_nowait(mypl.pop(0))
            Vch = get(self.client.voice_clients, guild=ctx.guild)
            if Vch.is_playing():
                Vch.stop()
                print(pq)
                Vch.play(fpcm(Q.get_nowait()))

        elif arg == "Skip":
            Vch = get(self.client.voice_clients, guild=ctx.guild)
            Vch.stop()
            print(Q)
            if mypl == []:
                load_s(mypl)
            song = mypl[0]
            print(song)
            try:
                song_n = song.replace("./songs/", "")
            except:
                song_n = song
            print(song_n)
            #Vch= ctx.guild.voice_client
            Vch.play(fpcm(song), after=Q.put_nowait(mypl.pop(0)))
            #Vch.source= discord.PCMVolumeTransformer(Vch.source)
            bmsg = await ctx.send(f"now playing {song_n}")
            await bmsg.delete(delay=5)

        elif arg.lower() == "stop":
            Vch = get(self.client.voice_clients, guild=ctx.guild)
            Vch.stop()
            await ctx.send("OK")

        # # Downloading songs
        elif arg == "dl":
            if (ctx.author.id == 444806806682730496):
                ydl_opts = {
                    'format':
                    'bestaudio/best',
                    'noplaylist':
                    True,
                    'outtmpl':
                    './songs/%(title)s.%(ext)s',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                    }],
                }
                bsmg = await ctx.send("畏まりました ...")
                with ytdl(ydl_opts) as dl:
                    print('Downloading audio now.\n')
                    dl.extract_info(url=link)
                    #  dl.download(url) # no use?
                    await bsmg.delete()
                    bmsg = await ctx.send("はい!")

            ## from StackOverflow answer
        #      player = await Vch.create_ytdl_player(url)
        #      await Q.put(player)
            else:
                print(ctx.author.id)
                await ctx.send("Denied!")

        elif arg == "mypl":
            em = discord.Embed(title="my playlist", description=mypl)
            bmsg = await ctx.send(embed=em)
            await bmsg.delete(delay=10)

        elif arg.lower() in ("playlist", "pl", "queue", "q", "المشغل"):
            #items = [Q.get_nowait() for i in range(Q.qsize())]
            em = discord.Embed(title="Current Playlist",
                               description=list(Q._queue),
                               colour=56550)
            await ctx.send(embed=em)

        elif arg.lower() in ("pause", "resume", "اکمل"):
            if ctx.guild.voice_client.is_paused():
                ctx.guild.voice_client.resume()
                bmsg = await ctx.send("resuming")
                await bmsg.delete(delay=3)
            else:
                ctx.guild.voice_client.pause()
                bmsg = await ctx.send("pausing")
                await bmsg.delete(delay=3)

        elif arg.lower() in ("leave", "l", "ترک", "اوقف"):
            Vch = ctx.guild.voice_client
            Vch.cleanup()
            await Vch.disconnect()
            await ctx.message.add_reaction('✅')

        # # gotta see how should this work (am sure smth wrong)

        #state = await self.client.wait_for('on_voice_state_update', check=Vch)
    # if state:
    #     print("Done")

        else:
            bmsg = await ctx.send("no arg satisfied")
            await ctx.send("> music <join , play, stop, pause/resume>")
            await bmsg.delete(delay=7)

    # from somerandomapi doc

    @commands.hybrid_command(aliases=['lrc', 'lyric', 'lrcs'])
    @app_commands.guilds(gid)
    async def lyrics(self, ctx, *, arg):
        await ctx.typing()

        # em = discord.Embed(title=f"**Looking for {arg}...**")
        #arg.replace(' ', '+')
        #lrcdata = None
        #lyrc = ""
        #async with aiohttp.ClientSession() as lrcses:
        #    lrcgetlnk = await lrcses.get(
        #        somerandapi+'/lyrics?title={}'.format(arg))
        #    lrcdata = json.loads(await lrcgetlnk.text())
        #    lyrc = str(lrcdata['lyrics'])

        print(arg)
        #arg = parse.quote(arg) # url-encode the song provided so it can be passed on to the API

        arg.replace(' ', '+')
        async with aiohttp.ClientSession() as lrcses:
            async with lrcses.get(f'https://some-random-api.com/lyrics?title={arg}') as jsondata: # define jsondata and fetch from API
                print(jsondata)
                if not 300 > jsondata.status >= 200: # if an unexpected HTTP status code is recieved from the website, throw an error and come out of the command
                    return await ctx.send(f'Recieved poor status code of {jsondata.status}')

                lrcData = await jsondata.json() # load the json data into its json form

        if lrcData.get('error'): # checking if there is an error recieved by the API, and if there is then throwing an error message and returning out of the command
            return await ctx.send(f'Recieved unexpected error: {lrcData.get("error")}')

        songLyrics = lrcData['lyrics'] # the lyrics
        #songArtist = lrcData['author'] # the author's name
        #songTitle = lrcData['title'] # the song's title
        songThumbnail = lrcData['thumbnail']['genius'] # the song's picture/thumbnail
        em = discord.Embed(
            title=f"**{(str(lrcData['title']))}** by {(str(lrcData['author']))}",
            description= songLyrics[:3000]) # Limit to 3000 characters initially
        em.set_footer(text="{0}".format(ctx.message.author.name),
               icon_url=ctx.message.author.display_avatar)
        em.timestamp = datetime.now(timezone.utc)
        em.set_thumbnail(url = songThumbnail)
        
        try:
            for chunk in [songLyrics[i:i + 3000] for i in range(3000, len(songLyrics), 3000)]:
                em.description = chunk
                await ctx.send(embed=em)

        except discord.HTTPException:
            em = discord.Embed(
                title=
                f"**{(str(lrcData['title']))} by {(str(lrcData['author']))}**",
                description=songLyrics)
            em.set_footer(
                text="{0}\nID: {1}\n{2}".format(
                  ctx.message.author.name, ctx.message.author.id,
                  datetime.now(timezone.utc).strftime("%A, %B %d %Y at %I:%M:%S %p UTC")),  ## Doesn't show
                icon_url=ctx.message.author.display_avatar)
            em.set_thumbnail(url = songThumbnail)
            em.timestamp = datetime.now(timezone.utc)

        await ctx.send(embed=em)


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        print('\n', member, after)
        try:
            for vc in self.client.voice_clients:
                if before.channel.id == vc.channel.id:
                    if not after.channel:
                        if (len(vc.channel.members) < 2):
                            print("time to disconnect")
                            await vc.disconnect()
        except Exception as e:
            print(e)


async def setup(client):
    await client.add_cog(Music(client))