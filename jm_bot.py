import discord
from discord.ext import commands
import time
from mutagen.mp3 import MP3

TOKEN = 'NTA3OTIwMjU2NjQ4NjA5Nzk4.Dr3tdg.L-81C1cq1P8ml6gnxbhONdoDiCM'
bot = commands.Bot('!')

folder_name = 'soundfiles'
jm_file_names = ['cant_argue',
        'dont_give_a_f_about',
        'f_em_hes_dead_dude',   
        'f_you_kris',   
        'g_damit',  
        'hes_dead_now',     
        'lay_here', 
        'leg',  
        'lil_b',    
        'no_im_not',    
        'no_running_clash', 
        'oh_yeah',  
        'shit_in_mouth',    
        'shut-your-fin-mouth-rakky',    
        'shut_the_f_up_david',      
        'shut_your_fin_mouth_rakky',    
        'sorry_brah',   
        'why_name', 
        'ye_he_heah',   
        'yoooo_ok']
jm_index = 0

cody_file_names = ['cody1','cody2', 'cody3']
cody_index = 1

antonio_file_names = ['antonio1']
antonio_index=0

kris_file_names = ['kris1','kris2']
kris_index = 0

@bot.command(pass_context = True)
async def menu(ctx,arg1='blank'):
    chan = ctx.message.channel 
    if arg1 == 'jm':
        msg = 'For ' + arg1 + ' your options are: '
        for entry in jm_file_names:
            msg=msg+(entry + ", ")
        msg = msg[0:len(msg)-2]
        msg=msg+('.')
    elif arg1 == 'cody':
        msg = 'For ' + arg1 + ' your options are: '
        for entry in cody_file_names:
            msg=msg+(entry + ", ")
        msg = msg[0:len(msg)-2]
        msg=msg+('.')
    elif arg1 == 'antonio':
        msg = 'For ' + arg1 + ' your options are: '
        for entry in antonio_file_names:
            msg = msg+(entry + ", ")
        msg=msg[0:len(msg)-2]
        msg=msg+('.')
    elif arg1 == 'kris': 
        msg = 'For ' + arg1 + ' your options are: '
        for entry in kris_file_names:
            msg = msg+(entry + ", ")
        msg = msg[0:len(msg)-2]
        msg=msg+('.')
        await bot.send_message(chan,msg)
    else:
        msg = 'You need to enter an argument (e.g. jm, cody, antonio, kris).'
    await bot.send_message(chan,msg)

@bot.command(pass_context = True)
async def jm(ctx,arg1='blank'):
    global jm_index
    filename = folder_name + '/' + jm_file_names[jm_index]+'.mp3'
    for name in jm_file_names:
        if arg1 == name:
            filename = 'soundfiles/'+name+'.mp3'
            jm_index = jm_index-1
    senders_voice_chan = ctx.message.author.voice.voice_channel
    voice = await bot.join_voice_channel(senders_voice_chan) 
    player = voice.create_ffmpeg_player(filename)
    player.volume = 2
    player.start()
    time.sleep(MP3(filename).info.length+1)
    player.stop()
    await voice.disconnect()
    jm_index = jm_index + 1
    if jm_index == len(jm_file_names):
        jm_index = 0

@bot.command(pass_context = True)
async def antonio(ctx,arg1='blank'):
    global antonio_index
    filename = folder_name + '/' + antonio_file_names[antonio_index]+'.mp3'
    for name in antonio_file_names:
        if arg1 == name:
            filename = 'soundfiles/'+name+'.mp3'
            antonio_index = antonio_index-1
    senders_voice_chan = ctx.message.author.voice.voice_channel
    voice = await bot.join_voice_channel(senders_voice_chan) 
    player = voice.create_ffmpeg_player(filename)
    player.volume = 2
    player.start()
    time.sleep(MP3(filename).info.length+1)
    player.stop()
    await voice.disconnect()
    antonio_index = antonio_index + 1
    if antonio_index == len(antonio_file_names):
        antonio_index = 0

@bot.command(pass_context = True)
async def cody(ctx,arg1='blank'):
    global cody_index
    filename = folder_name + '/' + cody_file_names[cody_index]+'.mp3'
    for name in cody_file_names:
        if arg1 == name:
            filename = 'soundfiles/'+name+'.mp3'
            cody_index = cody_index-1
    senders_voice_chan = ctx.message.author.voice.voice_channel
    voice = await bot.join_voice_channel(senders_voice_chan) 
    player = voice.create_ffmpeg_player(filename)
    player.volume = 2
    player.start()
    time.sleep(MP3(filename).info.length+1)
    player.stop()
    await voice.disconnect()
    cody_index = cody_index + 1
    if cody_index == len(cody_file_names):
        cody_index = 0
 
@bot.command(pass_context = True)
async def kris(ctx,arg1='blank'):
    global kris_index
    filename = folder_name + '/' + kris_file_names[kris_index]+'.mp3'
    for name in kris_file_names:
        if arg1 == name:
            filename = 'soundfiles/'+name+'.mp3'
            kris_index = kris_index-1
    senders_voice_chan = ctx.message.author.voice.voice_channel
    voice = await bot.join_voice_channel(senders_voice_chan) 
    player = voice.create_ffmpeg_player(filename)
    player.volume = 2
    player.start()
    time.sleep(MP3(filename).info.length+1)
    player.stop()
    await voice.disconnect()
    kris_index = kris_index + 1
    if kris_index == len(kris_file_names):
        kris_index = 0
 
@bot.command(pass_context = True)
async def leave(ctx):
    print('good bye')
    await bot.logout()

@bot.event
async def on_ready():
    print('all good')
    
bot.run(TOKEN)


