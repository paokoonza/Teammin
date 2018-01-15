# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, goslate
import timeit
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

cl = LINETCR.LINE()
cl.login(token="EoYBFGs3Gv8O1M8RLpca.OCTUHf+O8MrV6kxfKrHb/G.z3kvUo6SVtZSG+yEyawyzv6AjGtM7/TH8j2Ejn3KnpA=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EoqhM018YneEfe3swTYa.gvkdf5H6cMllyS3Mf6HhAG.2OnRzV5sG0/NK7Ug9AdAbClr9F27Eq5D5FUTPyFcDJY=")
ki2 = LINETCR.LINE()
ki2.login(token="EoHlnySU3i7f00sxWXQ0.zdI8/e53h+Gr0l8gt33maa.4PYKdbQikQ6fkqBBxN98k2k4xJe++gaeLPPK3pulx/I=")
ki3 = LINETCR.LINE()
ki3.login(token="EoHDaELez8W0b7b1KOXb.n5G7h/7wTBF/rKTjoaAawW.75z0wOYCACqcV5f57JDgmqf+yyOUx+jSot+EXGO7siA=")
ki4 = LINETCR.LINE()
ki4.login(token="EoqMKld11oRA8Xw2lkG0.U2t3FkQ9wbgmWnBJrVtEea.orIxIxdH4k0bIWbXkI1wdeFHRVYfbu2Ytv00or4bba8=")
ki5 = LINETCR.LINE()
ki5.login(token="EoNQcqufWYdvGQpiF580.jIxNXWLPHbxxvm/gsLAeCa.pl+8+rsrpJordTOTXaDxuVceRrnpmCvPJilniJDJW40=")
ki6 = LINETCR.LINE()
ki6.login(token="Eo52Um185O30I2fLNOke.tjCuQHDZ+qlVZNls7BQ6dG.Is3+bMu92Y8honSJdpKAaNH4OglR5HLNV8jJBg3IUIY=")
ki7 = LINETCR.LINE()
ki7.login(token="Eo23ruSATdt7bzyyEEU2.OQqjB9dJhQErfsVfrONXyG.2vJWZIyiyPeOk6tF+ZBnxeacZh2DCmLfw/jmOg0YeYM=")
ki8 = LINETCR.LINE()
ki8.login(token="Eokvf1UaRrpeF6Nbxc06.U7Gvr9sujvBq7JF8IAZ7nG.N595QKqEnpWtl/ioFkOHQHPVmmy9UBKpsjXUWTYuiW8=")
ki9 = LINETCR.LINE()
ki9.login(token="EoJ1pDvZZ90YlsM8uli9.MTkPFefXHLbv67jvH0JCsq./Dz4MIp1zV7b1zlChPuZn37BnLrW/+230eMSUadvleA=")
#k1 = LINETCR.LINE()
#k1.login(token="ElPnycU0m5kbWsE4WMY8.w3lt0n6pZyNIA1Cg5iuXsa.JIj2F9BoHPYVP5EljNvRupmSxp3OikeuNt6XnxpvE6I=")
#k2 = LINETCR.LINE()
#k2.login(token="EmXVcunJZMBvWip0OKoe.IuKj+S9Ahdxwlcyl0cQZBG.muSem8aizk+KB3vwjt3ObSmRxXlMcYoRZ/AvseJaszU=")
#k3 = LINETCR.LINE()
#k3.login(token="Elj7dstUSrXzacIVHex6.RGPppIhe6yhXXmCypSkJLG.KKjzDbQcvEp9FQe2AnCErp2TJfwFlUDNuqqc+HxbT/Y=")
#k4 = LINETCR.LINE()
#k4.login(token="El2BE964wwxtTjbtSwi1.AqVGuThed1z3iBCzEYdfiq.wwCxmEWameUSHEaJWemSscJt5ZIjlmVSkx/jE9fu8l8=")
#k5 = LINETCR.LINE()
#k5.login(token="ElgCJH3ZxlDtZzuxlnY9.Z8Uft1RvKsctA+/NZgaLcq.yr6QZzuypdCGlQT9lAJ17G4ELL+ponCkYK1UKlWLEos=")
#k6 = LINETCR.LINE()
#k6.login(token="EmVMpod4CThjH6uUHg1f.kInfQ54Mi4RJffkq3R2jFW.9Y8RUgoiA958fDU1AL5bJr6lnPcFtwWzeG/8LepQdeQ=")
#k7 = LINETCR.LINE()
#k7.login(token="EmN9Zql9Hs7PsSq9GIe2.lQFA26xbAPsX++hYRB5h4G.9rSzcjK3dFAZFvBYS5ytU80m8Wu8h9++vsHDRxSakU4=")
#k8 = LINETCR.LINE()
#k8.login(token="EmIgD1qjbgqnvx1qSRi3.qoUck3O8nMbB0hQWUC9FuW.kxn2Ryycgxyo9SLwW+vlC36lgC9Iimi0j12I1ShqNXE=")
#k9 = LINETCR.LINE()
#k9.login(token="EmgaRuxR1YztMwWENtdc.wC1yV200noVrRtR5N4fZ+a.WKsnRpPa3IQylGyn2Hm1pt+kDi9chIB9whG7pBDvB5g=")
#w1 = LINETCR.LINE()
#w1.login(token="EmZQU7XyakMTTsfrzlT2.1xH9TLwpE1GnY8ZLiHH1aG.LWJ24xGAleyWYZ/mbalLAjdJIpk3txY1hlED3o10eFE=")
#w2 = LINETCR.LINE()
#w2.login(token="Emr8hkx9rB79XGOo3QF2.t4ShpfPA+VTMHr264nEtyG.Tk6FQkHS2MC3xEYb9LcOMSQ7i8oKHGI9awBwCPsmvdM=")
#w3 = LINETCR.LINE()
#w3.login(token="EmKAXb2L7lKvc6acJTR8.z3mtdrm6URZU1LLgGghtga.Qly+DPeeykzFSwcf8C+fdYJzPmY8jfO/0Fig2VPZzAU=")
#w4 = LINETCR.LINE()
#w4.login(token="EmZmXBwZz6ecu6vc16Ic.sncrornClaPsa625qfQuBa.2hOrbFdmqXaRGXp/X897kY0ejnDxVRVjJpGWuy8U9NQ=")
#w5 = LINETCR.LINE()
#w5.login(token="EmRYJ76nxYjfMtU74Dfd.lLkjwOgGIrFz8jchH6OaVq.zxO9BUZc841R03al68WeiRqCsk8VmJC5nQVgSHsgV1E=")
#w6 = LINETCR.LINE()
#w6.login(token="EmdiYB2BO5uFUwlQaPvc.7NKbmZk0JuIVEBZv+QoTxa.tD0TrlgGVwoGcMdmkjj3zNoUmY81olS6WNmYaqSjJxg=")
#w7 = LINETCR.LINE()
#w7.login(token="EmL3CJJje4cAzjYsm2J7.fKxhS/9fZTF6s9ajKYtgfW.S5I2jgWhQdWZpr5D3JLol2DZoF7hslfGiGWXvra56Rg=")
#w8 = LINETCR.LINE()
#w8.login(token="Emp1bNlYZ2dgLB5yScl4.1e1R+OL5AgJVIZhWgMANba.gqPMVwITOHKDFl5rdF0ErUKgSZL+1221B1nOaxjyGj4=")
#w9 = LINETCR.LINE()
#w9.login(token="EmgVC67GIxvNWThWCln5.3pUwiYo9XLMnzgD40hGk1q.SwFa//qU6QHek609Z2Q4bIL4kVhtY2Jud59cLKqPSkk=")
#l1 = LINETCR.LINE()
#l1.login(token="EmdwvGrs9sFZsVhmKYZ7.zW1gn0bInHhxQzmhw3KNfW.Vy6m1MOIMQY9NQx5raUHfr1q6b6DI0HnKdo6JBNeCXU=")
#l2 = LINETCR.LINE()
#l2.login(token="EmKY6EyzlZtqKjHXq5y4.5xxiO4FRSRxP/7U73InJra.GKCtwR8ie+gE4DKKFXF8mpy0/Qu5J7k/4TujDcJa6q8=")
#l3 = LINETCR.LINE()
#l3.login(token="EmyU0zraBEKTNMGqNLvb.ex0v08tTcRRWci1liDHaoW.HU9CeNnqtB5dxmr5IsdxifE7bFxON82YI7btw7PNCqk=")
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage =""" ====[Self Bots PHET HECK BOT]====

              ༺•㏒ ᴳᵘ ᵀᵃʳ ᴾʰᵉᵗ ㏒•༻

❂͜͡☆➣ [Id]
❂͜͡☆➣ [Mid]
❂͜͡☆➣ [Me] 
❂͜͡☆➣ [TL 「Text」
❂͜͡☆➣ [MyName]
❂͜͡☆➣ [Gift]
❂͜͡☆➣ [Mid 「mid」
❂͜͡☆➣ [Group id]
❂͜͡☆➣ [Group cancel]
❂͜͡☆➣ [album 「id」]
❂͜͡☆➣ [Hapus album 「id」
❂͜͡☆➣ [Contact on] 
❂͜͡☆➣ [Contact off] 
❂͜͡☆➣ [Auto join on] 
❂͜͡☆➣ [Auto join off] 
❂͜͡☆➣ [Group cancel]
❂͜͡☆➣ [Auto leave on] 
❂͜͡☆➣ [Auto leave off]
❂͜͡☆➣ [Auto add on/off]
❂͜͡☆➣ [Bc ginfo]]
❂͜͡☆➣ [Jam on]
❂͜͡☆➣ [Jam off]
❂͜͡☆➣ [Jam say]
❂͜͡☆➣ [All Bot Me]
❂͜͡☆➣ [Ban:on] 
❂͜͡☆➣ [Unban:on]
❂͜͡☆➣ [Banlist]
❂͜͡☆➣ [Com on]
❂͜͡☆➣ [Com set]
❂͜͡☆➣ [Mcheck] 
❂͜͡☆➣ [Message Confirmation] 
❂͜͡☆➣ [Mybio: 「Isi Bio」]  
❂͜͡☆➣ [Allbio: 「Isi Bio bot」] 

       ༺•㏒ Instruction Room ㏒•༻

❂͜͡☆➣ [Link on]
❂͜͡☆➣ [Link off] 
❂͜͡☆➣ [Invite「mid」] 
❂͜͡☆➣ [Kmid: Kick by mid] 
❂͜͡☆➣ [Ginfo] 
❂͜͡☆➣ [Cancel]
❂͜͡☆➣ [Backup]
❂͜͡☆➣ [Gn 「Nama grup」
❂͜͡☆➣ [Gurl]
❂͜͡☆➣ [gurl「kelompok ID
❂͜͡☆➣ [Phet Tag All]
❂͜͡☆➣ [NK:]
❂͜͡☆➣ [PK @]
❂͜͡☆➣ [PKK 「nama]
❂͜͡☆➣ [Hack @] = [Hack]
❂͜͡☆➣ [Ban:]
❂͜͡☆➣ [Unban:]
❂͜͡☆➣ [Protect on]
❂͜͡☆➣ [qrprotect on/off]
❂͜͡☆➣ [Inviteprotect on]
❂͜͡☆➣ [Cancelprotect on]
❂͜͡☆➣ [Speed Sp / Bot Sp]
❂͜͡☆➣ [KK @]
❂͜͡☆➣ [Bot Me]
❂͜͡☆➣ [Me5 / Me10 / Me20]

     ༺•㏒ COMMAND Protect ㏒•༻

❂͜͡☆➣ [Pb all]
❂͜͡☆➣ [Pb Key]
❂͜͡☆➣ [Pb1-30 in]
❂͜͡☆➣ [Pb1-30 bye]
❂͜͡☆➣ [Respons]
❂͜͡☆➣ [Bye]        
❂͜͡☆➣ [Bye bot]
❂͜͡☆➣ [Go go][#Phet10]]        
❂͜͡☆➣ [KK1- KK3 / KKK / PPK]
        
  
       ☆ Ķ͈̤̱͎̱̤̞̭͂̐͒́̀͗͞Ị̵̻̝̘͍͛̏̃͊̉͠ T̩͖͎̹̫͈̿̆̏́̑́S̤̲̯̤̹̲̲̘̏̋̈́̿͒ͅŲ̶̼̲̺̣̬̔̿͐̾̾͘Ṇ̶̨̛̲̭̝̲̝̪̎̾̈́͘͢͜͞É͎̱̺̜̐̀̿͘̕̕͢  B̴̡̛͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠O̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅT Ç̵͔̟̫̰̮̺̟̥̂̋̂͋͐͛͑̔̚̚O̷̧̺̠̰̳̿́͆̕̕͠ͅ N̶͖̜̻̰͍̮̼̒́̐̑͒́̕ͅŢ̢̯̱͕̠͙̤̙̄̂͗̊̈́̕R̶̛̙̩̱̗̯͌̈͆̆Ơ̴̡͈̖̺͖̙̝̩̞̐̂̀͂̏̚͟͠L̸̡̩̣̲̣̜̊̑̾̾͊̃͘͜ͅ  ☆


[By.❦〖Pђëŧ〗☞ᵀËÄMທஇລ❂قB❂T✓]
"""
helo=""

KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
#k1mid = k1.getProfile().mid
#k2mid = k2.getProfile().mid
#k3mid = k3.getProfile().mid
#k4mid = k4.getProfile().mid
#k5mid = k5.getProfile().mid
#k6mid = k6.getProfile().mid
#k7mid = k7.getProfile().mid
#k8mid = k8.getProfile().mid
#k9mid = k9.getProfile().mid
#w1mid = w1.getProfile().mid
#w2mid = w2.getProfile().mid
#w3mid = w3.getProfile().mid
#w4mid = w4.getProfile().mid
#w5mid = w5.getProfile().mid
#w6mid = w6.getProfile().mid
#w7mid = w7.getProfile().mid
#w8mid = w8.getProfile().mid
#w9mid = w9.getProfile().mid
#l1mid = l1.getProfile().mid
#l2mid = l2.getProfile().mid
#l3mid = l3.getProfile().mid
Bots = ["ua1cb6e845fe8f2646fe8a5c5911841fa",mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid]
admsa = "ua1cb6e845fe8f2646fe8a5c5911841fa"
admin = "ua1cb6e845fe8f2646fe8a5c5911841fa"
wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"[SELFBOT PHET HACK BOT]",
    "lang":"JP",
    "comment":"Auto Like by\n\n[SELFBOT PHET HACK BOT]",
    "commentOn":False,
    "likeOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"มินทีมทดลองบอท ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "Notifed":True,
    "Notifedbot":True,    
    "kickMention":False,
    "detectMention":True,    
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
    
setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ua1cb6e845fe8f2646fe8a5c5911841fa":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)


        if op.type == 15:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName + "\n[เเล้วพบกันใหม่นะ]\n" + group.name
        if op.type == 15:
            if op.param2 in Bots:
                return
            random.choice(KAC).sendText(op.param1, "Good Bye\n\n[By.มินทีมทดลองบอท]")
            print "MEMBER HAS LEFT THE GROUP"
        if op.type == 17:
            if op.param2 in Bots:
                return
            random.choice(KAC).sendText(op.param1, "Welcome 􀜁􀄯􏿿\n\n[By.มินทีมทดลองบอท]")
            print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            group = cl.getGroup(op.param1)
            cb = Message()
            cb.to = op.param1
            cb.text = cl.getContact(op.param2).displayName + "\n[ยินดีต้อนรับครับ]\n" + group.name
            cl.sendMessage(cb)



















        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     l3.findAndAddContactsByMid(target)
                                     l3.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited this nigga💋: \n➡" + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower()  == 'help':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif "น้องตูน" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                ki.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                ki2.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                ki3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                ki5.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                cl.sendMessage(msg)
                k1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                cl.sendMessage(msg)
                k2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                cl.sendMessage(msg)
                k3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                cl.sendMessage(msg)
                k4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                cl.sendMessage(msg)
                k5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k6mid}
                cl.sendMessage(msg)
                k6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k7mid}
                cl.sendMessage(msg)
                k7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k8mid}
                cl.sendMessage(msg)
                k8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k9mid}
                cl.sendMessage(msg)
                k9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w1mid}
                cl.sendMessage(msg)
                w1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w2mid}
                cl.sendMessage(msg)
                w2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w3mid}
                cl.sendMessage(msg)
                w3.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w4mid}
                cl.sendMessage(msg)
                w4.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w5mid}
                cl.sendMessage(msg)
                w5.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w6mid}
                cl.sendMessage(msg)
                w6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w7mid}
                cl.sendMessage(msg)
                w7.sendMessage(msg) 
                msg.contentType = 13
                msg.contentMetadata = {'mid': w8mid}
                cl.sendMessage(msg)
                w8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w9mid}
                cl.sendMessage(msg)
                w9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l1mid}
                cl.sendMessage(msg)
                l1.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l2mid}
                cl.sendMessage(msg)
                l2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l3mid}
                cl.sendMessage(msg)
                l3.sendMessage(msg)
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': l4mid}
#                l4.sendMessage(msg)
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': l5mid}
#                l5.sendMessage(msg)
            elif "Pb1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                ki.sendMessage(msg)
            elif "Pb2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                ki2.sendMessage(msg)
            elif "Pb3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                ki3.sendMessage(msg)
            elif "Pb4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                ki4.sendMessage(msg)
            elif "Pb5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                ki5.sendMessage(msg)
            elif "Pb6" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                ki6.sendMessage(msg)
            elif "Pb7" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                ki7.sendMessage(msg)
            elif "Pb8" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                ki8.sendMessage(msg)
            elif "Pb9" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                ki9.sendMessage(msg)
            elif "Pb10" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                cl.sendMessage(msg)
                k1.sendMessage(msg)
            elif "Pb11" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                cl.sendMessage(msg)
                k2.sendMessage(msg)
            elif "Pb12" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                cl.sendMessage(msg)
                k3.sendMessage(msg)
            elif "Pb13" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                cl.sendMessage(msg)
                k4.sendMessage(msg)
            elif "Pb14" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                cl.sendMessage(msg)
                k5.sendMessage(msg)
            elif "Pb15" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k6mid}
                cl.sendMessage(msg)
                k6.sendMessage(msg)
            elif "Pb16" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k7mid}
                cl.sendMessage(msg)
                k7.sendMessage(msg)
            elif "Pb17" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k8mid}
                cl.sendMessage(msg)
                k8.sendMessage(msg)
            elif "Pb18" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': k9mid}
                cl.sendMessage(msg)
                k9.sendMessage(msg)
            elif "Pb19" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w1mid}
                cl.sendMessage(msg)
                w1.sendMessage(msg)
            elif "Pb20" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w2mid}
                cl.sendMessage(msg)
                w2.sendMessage(msg)
            elif "Pb21" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w3mid}
                cl.sendMessage(msg)
                w3.sendMessage(msg) 
            elif "Pb22" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w4mid}
                cl.sendMessage(msg)
                w4.sendMessage(msg) 
            elif "Pb23" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w5mid}
                cl.sendMessage(msg)
                w5.sendMessage(msg) 
            elif "Pb24" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w6mid}
                cl.sendMessage(msg)
                w6.sendMessage(msg)
            elif "Pb25" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w7mid}
                cl.sendMessage(msg)
                w7.sendMessage(msg) 
            elif "Pb26" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w8mid}
                cl.sendMessage(msg)
                w8.sendMessage(msg)
            elif "Pb27" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': w9mid}
                cl.sendMessage(msg)
                w9.sendMessage(msg)
            elif "Pb28" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l1mid}
                cl.sendMessage(msg)
                l1.sendMessage(msg)
            elif "Pb29" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l2mid}
                cl.sendMessage(msg)
                l2.sendMessage(msg)
            elif "Pb30" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': l3mid}
                cl.sendMessage(msg)
                l3.sendMessage(msg)
#            elif "Pro31" == msg.text:
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': l4mid}
#                l4.sendMessage(msg)
#            elif "Pro32" == msg.text:
#                msg.contentType = 13
#                msg.contentMetadata = {'mid': l5mid}
#                l5.sendMessage(msg)
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)

            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '4'}
                msg.text = None
                ki3.sendMessage(msg)
            elif msg.text in ["All Bot Gift","Gift you"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
                ki4.sendMessage(msg)
                ki5.sendMessage(msg)
                ki6.sendMessage(msg)
                ki7.sendMessage(msg)
                ki8.sendMessage(msg)
                ki9.sendMessage(msg)
                k1.sendMessage(msg)
                k2.sendMessage(msg)
                k3.sendMessage(msg)
                k4.sendMessage(msg)
                k5.sendMessage(msg)
                k6.sendMessage(msg)
                k7.sendMessage(msg)
                k8.sendMessage(msg)
                k9.sendMessage(msg)
                w1.sendMessage(msg)
                w2.sendMessage(msg)
                w3.sendMessage(msg)
                w4.sendMessage(msg)
                w5.sendMessage(msg)
                w6.sendMessage(msg)
                w7.sendMessage(msg)
                w8.sendMessage(msg)
                w9.sendMessage(msg)
                l1.sendMessage(msg)
                l2.sendMessage(msg)
                l3.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text in ["Cancel","ยกเลิก"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites")
                        else:
                            cl.sendText(msg.to,"Invite people inside not")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "P1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "P2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "P3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "P4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "P5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
            elif "P6 mid" == msg.text:
                ki6.sendText(msg.to,ki6mid)
            elif "P7 mid" == msg.text:
                ki7.sendText(msg.to,ki7mid)
            elif "P8 mid" == msg.text:
                ki8.sendText(msg.to,ki8mid)
            elif "P9 mid" == msg.text:
                ki9.sendText(msg.to,ki9mid)
            elif "P10 mid" == msg.text:
                k1.sendText(msg.to,k1mid)
            elif "P11 mid" == msg.text:
                k2.sendText(msg.to,k2mid)
            elif "P12 mid" == msg.text:
                k3.sendText(msg.to,k3mid)
            elif "P13 mid" == msg.text:
                k4.sendText(msg.to,k4mid)
            elif "P14 mid" == msg.text:
                k5.sendText(msg.to,k5mid)
            elif "P15 mid" == msg.text:
                k6.sendText(msg.to,k6mid)
            elif "P16 mid" == msg.text:
                k7.sendText(msg.to,k7mid)
            elif "P17 mid" == msg.text:
                k8.sendText(msg.to,k8mid)
            elif "P18 mid" == msg.text:
                k9.sendText(msg.to,k9mid)
            elif "P19 mid" == msg.text:
                w1.sendText(msg.to,w1mid)
            elif "P20 mid" == msg.text:
                w2.sendText(msg.to,w2mid)
            elif "P21 mid" == msg.text:
                w3.sendText(msg.to,w3mid)
            elif "P22 mid" == msg.text:
                w4.sendText(msg.to,w4mid)
            elif "P23 mid" == msg.text:
                w5.sendText(msg.to,w5mid)
            elif "P24 mid" == msg.text:
                w6.sendText(msg.to,w6mid)
            elif "P25 mid" == msg.text:
                w7.sendText(msg.to,w7mid)
            elif "P26 mid" == msg.text:
                w8.sendText(msg.to,w8mid)
            elif "P27 mid" == msg.text:
                w9.sendText(msg.to,w9mid)
            elif "P28 mid" == msg.text:
                l1.sendText(msg.to,l1mid)
            elif "P29 mid" == msg.text:
                l2.sendText(msg.to,l2mid)
            elif "P30 mid" == msg.text:
                l3.sendText(msg.to,l3mid)
#            elif "Pro31 mid" == msg.text:
#                l4.sendText(msg.to,l4mid)
#            elif "Pro32 mid" == msg.text:
#                l5.sendText(msg.to,l5mid)
            elif "Bot mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                k1.sendText(msg.to,k1mid)
                k2.sendText(msg.to,k2mid)
                k3.sendText(msg.to,k3mid)
                k4.sendText(msg.to,k4mid)
                k5.sendText(msg.to,k5mid)
                k6.sendText(msg.to,k6mid)
                k7.sendText(msg.to,k7mid)
                k8.sendText(msg.to,k8mid)
                k9.sendText(msg.to,k9mid)
                w1.sendText(msg.to,w1mid)
                w2.sendText(msg.to,w2mid)
                w3.sendText(msg.to,w3mid)
                w4.sendText(msg.to,w4mid)
                w5.sendText(msg.to,w5mid)
                w6.sendText(msg.to,w6mid)
                w7.sendText(msg.to,w7mid)
                w8.sendText(msg.to,w8mid)
                w9.sendText(msg.to,w9mid)
                l1.sendText(msg.to,l1mid)
                l2.sendText(msg.to,l2mid)
                l3.sendText(msg.to,l3mid)
#                l4.sendText(msg.to,l4mid)
#                l5.sendText(msg.to,l5mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "ชื่อบอททั้งหมด:" in msg.text:
                string = msg.text.replace("ชื่อบอททั้งหมด:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k6.getProfile()
                    profile.displayName = string
                    k6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k7.getProfile()
                    profile.displayName = string
                    k7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k8.getProfile()
                    profile.displayName = string
                    k8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = k9.getProfile()
                    profile.displayName = string
                    k9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w1.getProfile()
                    profile.displayName = string
                    w1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w2.getProfile()
                    profile.displayName = string
                    w2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w3.getProfile()
                    profile.displayName = string
                    w3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w4.getProfile()
                    profile.displayName = string
                    w4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w5.getProfile()
                    profile.displayName = string
                    w5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w6.getProfile()
                    profile.displayName = string
                    w6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w7.getProfile()
                    profile.displayName = string
                    w7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w8.getProfile()
                    profile.displayName = string
                    w8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = w9.getProfile()
                    profile.displayName = string
                    w9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = l1.getProfile()
                    profile.displayName = string
                    l1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = l2.getProfile()
                    profile.displayName = string
                    l2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = l3.getProfile()
                    profile.displayName = string
                    l3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l4.getProfile()
#                    profile.displayName = string
#                    l4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 20:
#                    profile = l5.getProfile()
#                    profile.displayName = string
#                    l5.updateProfile(profile)
            elif "ตัสบอททั้งหมด:" in msg.text:
                string = msg.text.replace("ตัสบอททั้งหมด:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k1.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k2.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k3.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k4.getProfile()
                    profile.statusMessage = string
                    k4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k5.getProfile()
                    profile.statusMessage = string
                    k5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k6.getProfile()
                    profile.statusMessage = string
                    k6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k7.getProfile()
                    profile.statusMessage = string
                    k7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k8.getProfile()
                    profile.statusMessage = string
                    k8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = k9.getProfile()
                    profile.statusMessage = string
                    k9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w1.getProfile()
                    profile.statusMessage = string
                    w1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w2.getProfile()
                    profile.statusMessage = string
                    w2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w3.getProfile()
                    profile.statusMessage = string
                    w3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w4.getProfile()
                    profile.statusMessage = string
                    w4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w5.getProfile()
                    profile.statusMessage = string
                    w5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w6.getProfile()
                    profile.statusMessage = string
                    w6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w7.getProfile()
                    profile.statusMessage = string
                    w7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w8.getProfile()
                    profile.statusMessage = string
                    w8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = w9.getProfile()
                    profile.statusMessage = string
                    w9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l1.getProfile()
                    profile.statusMessage = string
                    l1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l2.getProfile()
                    profile.statusMessage = string
                    l2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = l3.getProfile()
                    profile.statusMessage = string
                    l3.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 500:
#                    profile = l4.getProfile()
#                    profile.statusMessage = string
#                    l4.updateProfile(profile)
#                if len(string.decode('utf-8')) <= 500:
#                    profile = l5.getProfile()
#                    profile.statusMessage = string
#                    l5.updateProfile(profile)

#---------------------------------------------------------
            elif "1pro: " in msg.text:
                string = msg.text.replace("1pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "2pro: " in msg.text:
                string = msg.text.replace("2pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "3pro: " in msg.text:
                string = msg.text.replace("3pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "4pro: " in msg.text:
                string = msg.text.replace("4pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "5pro: " in msg.text:
                string = msg.text.replace("5pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "6pro: " in msg.text:
                string = msg.text.replace("6pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "7pro: " in msg.text:
                string = msg.text.replace("7pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "8pro: " in msg.text:
                string = msg.text.replace("8pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "9pro: " in msg.text:
                string = msg.text.replace("9pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "10pro: " in msg.text:
                string = msg.text.replace("10pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k1.getProfile()
                    profile.displayName = string
                    k1.updateProfile(profile)
                    k1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "11pro: " in msg.text:
                string = msg.text.replace("11pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k2.getProfile()
                    profile.displayName = string
                    k2.updateProfile(profile)
                    k2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "12pro: " in msg.text:
                string = msg.text.replace("12pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k3.getProfile()
                    profile.displayName = string
                    k3.updateProfile(profile)
                    k3.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "13pro: " in msg.text:
                string = msg.text.replace("13pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k4.getProfile()
                    profile.displayName = string
                    k4.updateProfile(profile)
                    k4.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "14pro: " in msg.text:
                string = msg.text.replace("14pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k5.getProfile()
                    profile.displayName = string
                    k5.updateProfile(profile)
                    k5.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "15pro: " in msg.text:
                string = msg.text.replace("15pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k6.getProfile()
                    profile.displayName = string
                    k6.updateProfile(profile)
                    k6.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "16pro: " in msg.text:
                string = msg.text.replace("16pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k7.getProfile()
                    profile.displayName = string
                    k7.updateProfile(profile)
                    k7.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "17pro: " in msg.text:
                string = msg.text.replace("17pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k8.getProfile()
                    profile.displayName = string
                    k8.updateProfile(profile)
                    k8.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "18pro: " in msg.text:
                string = msg.text.replace("18pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = k9.getProfile()
                    profile.displayName = string
                    k9.updateProfile(profile)
                    k9.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "19pro: " in msg.text:
                string = msg.text.replace("19pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = w1.getProfile()
                    profile.displayName = string
                    w1.updateProfile(profile)
                    w1.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "20pro: " in msg.text:
                string = msg.text.replace("20pro: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = w2.getProfile()
                    profile.displayName = string
                    w2.updateProfile(profile)
                    w2.sendText(msg.to,"􀜁􀇔􏿿Update Names👉" + string + "👈")
#--------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off")
                    else:
                        cl.sendText(msg.to,"It is already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off")
                    else:
                        cl.sendText(msg.to,"already Close")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on ")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on ")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON")
                    else:
                        cl.sendText(msg.to,"It is already On")
            elif msg.text in ["Allprotect on","#เปิดป้องกัน"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on ")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite on")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel on ")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect on")
                    else:
                        cl.sendText(msg.to,"Already on")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on ")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR on")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Allprotect off","#ปิดป้องกัน"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite off")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel off ")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off ")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect off")
                    else:
                        cl.sendText(msg.to,"Already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Is already open")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on")
                    else:
                        cl.sendText(msg.to,"Sudah off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Is already close")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on")
                    else:
                        cl.sendText(msg.to,"on")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"Off")
            elif msg.text.lower() == 'set':
                md = "✯= ꧁ 🐯हईທຮຮๅજईह🐯 ꧂=✯\n\n"
                if wait["contact"] == True: md+="􀜁􀇔􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Contact:off 􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀜁􀇔􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md+="􀜁􀇔􏿿 Auto Join:off 􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇔􏿿 Auto cancel: " + str(wait["autoCancel"]["members"]) + " 􀜁􀄯􏿿 \n"
                else: md+="􀜁􀇔􏿿 Group cancel 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇔􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="??􀇔􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀜁􀇔􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀜁􀇔􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto add:off 􀜁􀄰􏿿\n"
                if wait["commentOn"] == True: md+="􀜁􀇔􏿿 Auto komentar:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto komentar:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀜁􀇔􏿿 Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Protect:off 􀜁􀄰􏿿\n"
                if wait["linkprotect"] == True: md+="􀜁􀇔􏿿 Link Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Link Protect:off 􀜁􀄰􏿿\n"
                if wait["inviteprotect"] == True: md+="􀜁􀇔􏿿 Invitation Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Invitation Protect:off 􀜁􀄰􏿿\n"
                if wait["cancelprotect"] == True: md+="􀜁􀇔􏿿 Cancel Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Cancel Protect:off 􀜁􀄰􏿿\n"
                if wait["likeOn"] == True: md+="􀜁􀇔􏿿 Auto like:on 􀜁􀄯􏿿\n"
                else:md+="􀜁􀇔􏿿 Auto like:off 􀜁􀄰􏿿\n" 
                if wait["Notifed"] == True: md+="􀬁􀆐􏿿 Notifed : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifed : off 􀜁􀄰􏿿\n"
                if wait["Notifedbot"] == True: md+="􀬁􀆐􏿿 Notifedbot : on 􀜁􀄯􏿿\n"
                else:md+="􀬁􀆐􏿿 Notifedbot : off 􀜁􀄰􏿿\n"                
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            
            elif msg.text in ["Like:on","Llke on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done.")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already")
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done.")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Alread")
                        
            elif msg.text in ["Add on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On")
            elif msg.text in ["Add off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off")
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                cl.sendText(msg.to,"We changed the message")
            elif "Help set: " in msg.text:
                wait["help"] = msg.text.replace("Help set: ","")
                cl.sendText(msg.to,"We changed the Help👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Kami mengubah pesan🛡")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Com","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"✯===== ꧁ Auto Message ꧂ =====✯\n\n[SELFBOT PHET HACK BOT]\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Coms set:" in msg.text:
                c = msg.text.replace("Coms set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Coms","Comment"]:
                cl.sendText(msg.to,"✯===== ꧁ Auto Message ꧂=====✯\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Sudah On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Hal ini sudah off🛡")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say: " in msg.text:
                n = msg.text.replace("Jam say: ","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'meupname':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"༺%H:%M༻")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif msg.text == "ตั้งเวลา":
                if msg.toType == 2:
                    cl.sendText(msg.to, "โปรดรอ..กรุณาพิมพ์ อ่าน \n\n[ตั้งเวลาอ่านล่าสุด]:" + datetime.now().strftime('\n%Y/%m/%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "อ่าน":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "       [SELFBOT PHET HACK BOT]\n\n==============================\nActive readers:%s\n\n\n\nPassive readers:\n%s\n\n==============================\nIn the last seen point:\n[%s]\n==============================\nBy:เพชร ทีมทดลองบอท" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Auto set reading point in:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "Reading point has not been set.")

#-----------------------[Add Staff Section]------------------------
            elif "Bot add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Bot add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Bot de @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Bot de @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","Bot??"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list: ")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------------------
            elif "Wcginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)

            elif ("2PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("3PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("4PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki4.sendText(msg.to,"Error")
            elif ("5PK " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif "Bot@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    l3.sendMessage(msg)
            elif "Bot@@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    ki.sendMessage(msg)
                    ki2.sendMessage(msg)
                    ki3.sendMessage(msg)
                    ki4.sendMessage(msg)
                    ki5.sendMessage(msg)
                    ki6.sendMessage(msg)
                    ki7.sendMessage(msg)
                    ki8.sendMessage(msg)
                    ki9.sendMessage(msg)

            elif "Phet Say " in msg.text:
                                bctxt = msg.text.replace("Phet Say ","")
                                ki.sendText(msg.to,(bctxt))
                                ki2.sendText(msg.to,(bctxt))
                                ki3.sendText(msg.to,(bctxt))
                                ki4.sendText(msg.to,(bctxt))
                                ki5.sendText(msg.to,(bctxt))
                                ki6.sendText(msg.to,(bctxt))
                                ki7.sendText(msg.to,(bctxt))
                                ki8.sendText(msg.to,(bctxt))
                                ki9.sendText(msg.to,(bctxt))
                                k1.sendText(msg.to,(bctxt))
                                k2.sendText(msg.to,(bctxt))
                                k3.sendText(msg.to,(bctxt))
                                k4.sendText(msg.to,(bctxt))
                                k5.sendText(msg.to,(bctxt))
                                k6.sendText(msg.to,(bctxt))
                                k7.sendText(msg.to,(bctxt))
                                k8.sendText(msg.to,(bctxt))
                                k9.sendText(msg.to,(bctxt))
                                w1.sendText(msg.to,(bctxt))
                                w2.sendText(msg.to,(bctxt))
                                w3.sendText(msg.to,(bctxt))
                                w4.sendText(msg.to,(bctxt))
                                w5.sendText(msg.to,(bctxt))
                                w6.sendText(msg.to,(bctxt))
                                w7.sendText(msg.to,(bctxt))
                                w8.sendText(msg.to,(bctxt))
                                w9.sendText(msg.to,(bctxt))
                                l1.sendText(msg.to,(bctxt))
                                l2.sendText(msg.to,(bctxt))
                                l3.sendText(msg.to,(bctxt))


#----------------------------------------------------------------
            
#-----------------------------------------------------------
#-----------------------------------------------------------)
#----------------------ADMIN COMMAND----------------------------_ in admin:
            elif ("1PK " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ki.kickoutFromGroup(msg.to,[target])
                        except:
                            ki.sendText(msg.to,"Error")

            elif ("PK " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
                    
            elif "Phet@@" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 

            elif "PKK @" in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("PKK @","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("all","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                              targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:                            
                             if not target in Bots:
                                if not target in admin:
                                  try:
                                      klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,w1,w2,w3]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      print (msg.to,[g.mid])
                                  except:
                                      cl.sendText(msg.to,"Sukses Bosqu")
                                      cl.sendText(msg.to,"masih mauko sundala")

            elif msg.text in ["List group","Group Me","กลุ่มกู"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n -+GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif msg.text in ["Info grup","ค้างเชิญ"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    cl.sendText(msg.to,"===[List Details Group]===")
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = ki.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h = "[" + groups.name + "]\n -+GroupID : " + i + "\n[สมาชิก] : " + members + "\n[จำนวนค้างเชิญ] : " + pendings + "\n[ผู้สร้างกลุ่ม] : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h)
                        cl.sendText(msg.to,"|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    cl.sendText(msg.to,"===[List Details Groups Invited]===")
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j = "[" + groups.name + "]\n -+GroupID : " + i + "\n[สมาชิก] : " + members + "\n[จำนวนค้างเชิญ] : " + pendings + "\n[ผู้สร้างกลุ่ม] : " + groups.creator.displayName
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j)
                        cl.sendText(msg.to,"|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")

            elif "/รายละเอียด:" in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/รายละเอียด:","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
            
            elif "/ยกเลิกเชิญ:" in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("/ยกเลิกเชิญ:","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite","ยอมรับคำเชิญทั้งหมด"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "/Myname: " in msg.text:
                string = msg.text.replace("/Myname: ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)

            elif "/Mybio: " in msg.text:
                string = msg.text.replace("/Mybio: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio" + string)
            
            elif ("/Gname: " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("/Gname: ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Tidak Dapat Mengubah Nama Grup")

            elif "Kick:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite:" in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "/Hackk @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("/Hackk @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Profile copy.")
                                except Exception as e:
                                    print e
                                    
            elif "Botcopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Botcopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki.sendText(msg.to, "Copy done..")
                                    ki2.cloneContactProfile(target)
                                    ki2.sendText(msg.to, "Copy done..")
                                    ki3.cloneContactProfile(target)
                                    ki3.sendText(msg.to, "Copy done..")
                                    ki4.cloneContactProfile(target)
                                    ki4.sendText(msg.to, "Copy done..")
                                    ki5.cloneContactProfile(target)
                                    ki5.sendText(msg.to, "Copy done..")
                                    ki6.cloneContactProfile(target)
                                    ki6.sendText(msg.to, "Copy done..")
                                    ki7.cloneContactProfile(target)
                                    ki7.sendText(msg.to, "Copy done..")
                                    ki8.cloneContactProfile(target)
                                    ki8.sendText(msg.to, "Copy done..")
                                    ki9.cloneContactProfile(target)
                                    ki9.sendText(msg.to, "Copy done..")
                                    k1.cloneContactProfile(target)
                                    k1.sendText(msg.to, "Copy done..")
                                    k2.cloneContactProfile(target)
                                    k2.sendText(msg.to, "Copy done..")
                                    k3.cloneContactProfile(target)
                                    k3.sendText(msg.to, "Copy done..")
                                    k4.cloneContactProfile(target)
                                    k4.sendText(msg.to, "Copy done..")
                                    k5.cloneContactProfile(target)
                                    k5.sendText(msg.to, "Copy done..")
                                    k6.cloneContactProfile(target)
                                    k6.sendText(msg.to, "Copy done..")
                                    k7.cloneContactProfile(target)
                                    k7.sendText(msg.to, "Copy done..")
                                    k8.cloneContactProfile(target)
                                    k8.sendText(msg.to, "Copy done..")
                                    k9.cloneContactProfile(target)
                                    k9.sendText(msg.to, "Copy done..")
                                    w1.cloneContactProfile(target)
                                    w1.sendText(msg.to, "Copy done..")
                                    w2.cloneContactProfile(target)
                                    w2.sendText(msg.to, "Copy done..")
                                    w3.cloneContactProfile(target)
                                    w3.sendText(msg.to, "Copy done..")
                                    w4.cloneContactProfile(target)
                                    w4.sendText(msg.to, "Copy done..")
                                    w5.cloneContactProfile(target)
                                    w5.sendText(msg.to, "Copy done..")
                                    w6.cloneContactProfile(target)
                                    w6.sendText(msg.to, "Copy done..")
                                    w7.cloneContactProfile(target)
                                    w7.sendText(msg.to, "Copy done..")
                                    w8.cloneContactProfile(target)
                                    w8.sendText(msg.to, "Copy done..")
                                    w9.cloneContactProfile(target)
                                    w9.sendText(msg.to, "Copy done..")
                                    l1.cloneContactProfile(target)
                                    l1.sendText(msg.to, "Copy done..")
                                    l2.cloneContactProfile(target)
                                    l2.sendText(msg.to, "Copy done..")
                                    l3.cloneContactProfile(target)
                                    l3.sendText(msg.to, "Copy done..")
#                                    l4.cloneContactProfile(target)
#                                    k5.cloneContactProfile(target)
#                                    ki.sendText(msg.to, "Profile copy.")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["Mybackup","Mebb"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Ok..backup")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup","Botbb"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                    ki3.updateDisplayPicture(backup.pictureStatus)
                    ki3.updateProfile(backup)
                    ki4.updateDisplayPicture(backup.pictureStatus)
                    ki4.updateProfile(backup)
                    ki5.updateDisplayPicture(backup.pictureStatus)
                    ki5.updateProfile(backup)
                    ki6.updateDisplayPicture(backup.pictureStatus)
                    ki6.updateProfile(backup)
                    ki7.updateDisplayPicture(backup.pictureStatus)
                    ki7.updateProfile(backup)
                    ki8.updateDisplayPicture(backup.pictureStatus)
                    ki8.updateProfile(backup)
                    ki9.updateDisplayPicture(backup.pictureStatus)
                    ki9.updateProfile(backup)
                    k1.updateDisplayPicture(backup.pictureStatus)
                    k1.updateProfile(backup)
                    k2.updateDisplayPicture(backup.pictureStatus)
                    k2.updateProfile(backup)
                    k3.updateDisplayPicture(backup.pictureStatus)
                    k3.updateProfile(backup)
                    k4.updateDisplayPicture(backup.pictureStatus)
                    k4.updateProfile(backup)
                    k5.updateDisplayPicture(backup.pictureStatus)
                    k5.updateProfile(backup)
                    k6.updateDisplayPicture(backup.pictureStatus)
                    k6.updateProfile(backup)
                    k7.updateDisplayPicture(backup.pictureStatus)
                    k7.updateProfile(backup)
                    k8.updateDisplayPicture(backup.pictureStatus)
                    k8.updateProfile(backup)
                    k9.updateDisplayPicture(backup.pictureStatus)
                    k9.updateProfile(backup)
                    w1.updateDisplayPicture(backup.pictureStatus)
                    w1.updateProfile(backup)
                    w2.updateDisplayPicture(backup.pictureStatus)
                    w2.updateProfile(backup)
                    w3.updateDisplayPicture(backup.pictureStatus)
                    w3.updateProfile(backup)
                    w4.updateDisplayPicture(backup.pictureStatus)
                    w4.updateProfile(backup)
                    w5.updateDisplayPicture(backup.pictureStatus)
                    w5.updateProfile(backup)
                    w6.updateDisplayPicture(backup.pictureStatus)
                    w6.updateProfile(backup)
                    w7.updateDisplayPicture(backup.pictureStatus)
                    w7.updateProfile(backup)
                    w8.updateDisplayPicture(backup.pictureStatus)
                    w8.updateProfile(backup)
                    w9.updateDisplayPicture(backup.pictureStatus)
                    w9.updateProfile(backup)
                    l1.updateDisplayPicture(backup.pictureStatus)
                    l1.updateProfile(backup)
                    l2.updateDisplayPicture(backup.pictureStatus)
                    l2.updateProfile(backup)
                    l3.updateDisplayPicture(backup.pictureStatus)
                    l3.updateProfile(backup)
#                    l4.updateDisplayPicture(backup.pictureStatus)
#                    l4.updateProfile(backup)
#                    l5.updateDisplayPicture(backup.pictureStatus)
#                    l5.updateProfile(backup)
                    ki.sendText(msg.to, "Backup bot all")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

            elif "Bc:ct " in msg.text:
                bctxt = msg.text.replace("Bc:ct ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))

            elif "Bot:ct " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:ct ", "")
                b = ki.getAllContactIds()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getAllContactIds()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getAllContactIds()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getAllContactIds()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getAllContactIds()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                g = ki6.getAllContactIds()
                for manusia in g:
                    ki6.sendText(manusia, (bctxt))
                h = ki7.getAllContactIds()
                for manusia in h:
                    ki7.sendText(manusia, (bctxt))
                i = ki8.getAllContactIds()
                for manusia in i:
                    ki8.sendText(manusia, (bctxt))
                j = ki9.getAllContactIds()
                for manusia in j:
                    ki9.sendText(manusia, (bctxt))
                k = k1.getAllContactIds()
                for manusia in k:
                    k1.sendText(manusia, (bctxt))
                l = k2.getAllContactIds()
                for manusia in l:
                    k2.sendText(manusia, (bctxt))
                m = k3.getAllContactIds()
                for manusia in m:
                    k3.sendText(manusia, (bctxt))
                n = k4.getAllContactIds()
                for manusia in n:
                    k4.sendText(manusia, (bctxt))
                o = k5.getAllContactIds()
                for manusia in o:
                    k5.sendText(manusia, (bctxt))
                p = k6.getAllContactIds()
                for manusia in p:
                    k6.sendText(manusia, (bctxt))
                q = k7.getAllContactIds()
                for manusia in q:
                    k7.sendText(manusia, (bctxt))
                r = k8.getAllContactIds()
                for manusia in r:
                    k8.sendText(manusia, (bctxt))
                s = k9.getAllContactIds()
                for manusia in s:
                    k9.sendText(manusia, (bctxt))
                t = w1.getAllContactIds()
                for manusia in t:
                    w1.sendText(manusia, (bctxt))
                u = w2.getAllContactIds()
                for manusia in u:
                    w2.sendText(manusia, (bctxt))
                
            elif "Bc:grup " in msg.text:
                bctxt = msg.text.replace("Bc:grup ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, (bctxt))
            
            elif "Bot:grup " in msg.text:
              if msg.from_ in admin:
                bctxt = msg.text.replace("Bot:grup ", "")
                b = ki.getGroupIdsJoined()
                for manusia in b:
                    ki.sendText(manusia, (bctxt))
                c = ki2.getGroupIdsJoined()
                for manusia in c:
                    ki2.sendText(manusia, (bctxt))
                d = ki3.getGroupIdsJoined()
                for manusia in d:
                    ki3.sendText(manusia, (bctxt))
                e = ki4.getGroupIdsJoined()
                for manusia in e:
                    ki4.sendText(manusia, (bctxt))
                f = ki5.getGroupIdsJoined()
                for manusia in f:
                    ki5.sendText(manusia, (bctxt))
                g = ki6.getGroupIdsJoined()
                for manusia in g:
                    ki6.sendText(manusia, (bctxt))
                h = ki7.getGroupIdsJoined()
                for manusia in h:
                    ki7.sendText(manusia, (bctxt))
                i = ki8.getGroupIdsJoined()
                for manusia in i:
                    ki8.sendText(manusia, (bctxt))
                j = ki9.getGroupIdsJoined()
                for manusia in j:
                    ki9.sendText(manusia, (bctxt))
                k = k1.getGroupIdsJoined()
                for manusia in k:
                    k1.sendText(manusia, (bctxt))
                l = k2.getGroupIdsJoined()
                for manusia in l:
                    k2.sendText(manusia, (bctxt))
                m = k3.getGroupIdsJoined()
                for manusia in m:
                    k3.sendText(manusia, (bctxt))
                n = k4.getGroupIdsJoined()
                for manusia in n:
                    k4.sendText(manusia, (bctxt))
                o = k5.getGroupIdsJoined()
                for manusia in o:
                    k5.sendText(manusia, (bctxt))
                p = k6.getGroupIdsJoined()
                for manusia in p:
                    k6.sendText(manusia, (bctxt))
                q = k7.getGroupIdsJoined()
                for manusia in q:
                    k7.sendText(manusia, (bctxt))
                r = k8.getGroupIdsJoined()
                for manusia in r:
                    k8.sendText(manusia, (bctxt))
                s = k9.getGroupIdsJoined()
                for manusia in s:
                    k9.sendText(manusia, (bctxt))
                t = w1.getGroupIdsJoined()
                for manusia in t:
                    w1.sendText(manusia, (bctxt))
                u = w2.getGroupIdsJoined()
                for manusia in u:
                    w2.sendText(manusia, (bctxt))

            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 500:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 500:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'me20':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Mee"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"􀜁􀇔􏿿 My Creator 􀜁􀇔􏿿 ")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"􀜁􀇔􏿿 Dont Kick out From group 􀜁􀇔􏿿 ")
            
            elif "Mev" in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Mev","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif msg.text in ["#Clear grup","Byebot All","บอทออกทั้งหมด"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = k1.getGroupIdsJoined()
                gid = k2.getGroupIdsJoined()
                gid = k3.getGroupIdsJoined()
                gid = k4.getGroupIdsJoined()
                gid = k5.getGroupIdsJoined()
                gid = k6.getGroupIdsJoined()
                gid = k7.getGroupIdsJoined()
                gid = k8.getGroupIdsJoined()
                gid = k9.getGroupIdsJoined()
                gid = w1.getGroupIdsJoined()
                gid = w2.getGroupIdsJoined()
                gid = w3.getGroupIdsJoined()
                gid = w4.getGroupIdsJoined()
                gid = w5.getGroupIdsJoined()
                gid = w6.getGroupIdsJoined()
                gid = w7.getGroupIdsJoined()
                gid = w8.getGroupIdsJoined()
                gid = w9.getGroupIdsJoined()
                gid = l1.getGroupIdsJoined()
                gid = l2.getGroupIdsJoined()
                gid = l3.getGroupIdsJoined()
#                gid = l4.getGroupIdsJoined()
#                gid = l5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    k1.leaveGroup(i)
                    k2.leaveGroup(i)
                    k3.leaveGroup(i)
                    k4.leaveGroup(i)
                    k5.leaveGroup(i)
                    k6.leaveGroup(i)
                    k7.leaveGroup(i)
                    k8.leaveGroup(i)
                    k9.leaveGroup(i)
                    w1.leaveGroup(i)
                    w2.leaveGroup(i)
                    w3.leaveGroup(i)
                    w4.leaveGroup(i)
                    w5.leaveGroup(i)
                    w6.leaveGroup(i)
                    w7.leaveGroup(i)
                    w8.leaveGroup(i)
                    w9.leaveGroup(i)
                    l1.leaveGroup(i)
                    l2.leaveGroup(i)
                    l3.leaveGroup(i)
#                    l4.leaveGroup(i)
#                    l5.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif msg.text == "Ginfo":
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    cl.sendText(msg.to,md)
            
            elif msg.text == "Uni":
	            ki.sendText(msg.to,"Hai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
                    cl.sendText(msg.to,"Sorry")
            elif ".music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
            
            elif 'ขอเพลง ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ขอเพลง ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
            
            elif "BK @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("BK @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print e

            elif msg.text.lower() == 'bann':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            
            elif msg.text in ["Glist","Ginfomeall"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[★] %s\n" % (cl.getGroup(i).name +"→["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"▒▒▓█[List Group]█▓▒▒\n"+ h +"Total Group =" +"["+str(len(gid))+"]")

            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"Please send contact")
                
            elif ("Hack " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Mid @" in msg.text:
              if msg.from_ in admin:  
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass

            elif "Mymid" == msg.text:
                cl.sendText(msg.to,mid)

            elif msg.text in ["Link on"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  ")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = ki2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki2.getGroup(i).name + " | [ " + str(len (ki2.getGroup(i).members)) + " ]")
                ki2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = ki3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki3.getGroup(i).name + " | [ " + str(len (ki3.getGroup(i).members)) + " ]")
                ki3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S4glist"]:
                gs = ki4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki4.getGroup(i).name + " | [ " + str(len (ki4.getGroup(i).members)) + " ]")
                ki4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S5glist"]:
                gs = ki5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki5.getGroup(i).name + " | [ " + str(len (ki5.getGroup(i).members)) + " ]")
                ki5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S6glist"]:
                gs = ki6.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki6.getGroup(i).name + " | [ " + str(len (ki6.getGroup(i).members)) + " ]")
                ki6.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S7glist"]:
                gs = ki7.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki7.getGroup(i).name + " | [ " + str(len (ki7.getGroup(i).members)) + " ]")
                ki7.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S8glist"]:
                gs = ki8.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki8.getGroup(i).name + " | [ " + str(len (ki8.getGroup(i).members)) + " ]")
                ki8.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S9glist"]:
                gs = ki9.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki9.getGroup(i).name + " | [ " + str(len (ki9.getGroup(i).members)) + " ]")
                ki9.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S10glist"]:
                gs = k1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k1.getGroup(i).name + " | [ " + str(len (k1.getGroup(i).members)) + " ]")
                k1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S11glist"]:
                gs = k2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k2.getGroup(i).name + " | [ " + str(len (k2.getGroup(i).members)) + " ]")
                k2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S12glist"]:
                gs = k3.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k3.getGroup(i).name + " | [ " + str(len (k3.getGroup(i).members)) + " ]")
                k3.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S13glist"]:
                gs = k4.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k4.getGroup(i).name + " | [ " + str(len (k4.getGroup(i).members)) + " ]")
                k4.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S14glist"]:
                gs = k5.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k5.getGroup(i).name + " | [ " + str(len (k5.getGroup(i).members)) + " ]")
                k5.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S15glist"]:
                gs = k6.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k6.getGroup(i).name + " | [ " + str(len (k6.getGroup(i).members)) + " ]")
                k6.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S16glist"]:
                gs = k7.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k7.getGroup(i).name + " | [ " + str(len (k7.getGroup(i).members)) + " ]")
                k7.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S17glist"]:
                gs = k8.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k8.getGroup(i).name + " | [ " + str(len (k8.getGroup(i).members)) + " ]")
                k8.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S18glist"]:
                gs = k9.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (k9.getGroup(i).name + " | [ " + str(len (k9.getGroup(i).members)) + " ]")
                k9.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S19glist"]:
                gs = w1.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (w1.getGroup(i).name + " | [ " + str(len (w1.getGroup(i).members)) + " ]")
                w1.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S20glist"]:
                gs = w2.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (w2.getGroup(i).name + " | [ " + str(len (w2.getGroup(i).members)) + " ]")
                w2.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
                    
            elif msg.text == "บอทขอคลิป":
                    ki.sendText(msg.to,"nekopoi.host")
                    ki.sendText(msg.to,"sexvideobokep.com")
                    ki.sendText(msg.to,"memek.com")
                    ki.sendText(msg.to,"pornktube.com")
                    ki.sendText(msg.to,"faketaxi.com")
                    ki.sendText(msg.to,"videojorok.com")
                    ki.sendText(msg.to,"watchmygf.mobi")
                    ki.sendText(msg.to,"xnxx.com")
                    ki.sendText(msg.to,"pornhd.com")
                    ki.sendText(msg.to,"xvideos.com")
                    ki.sendText(msg.to,"vidz7.com")
                    ki.sendText(msg.to,"m.xhamster.com")
                    ki.sendText(msg.to,"xxmovies.pro")
                    ki.sendText(msg.to,"youporn.com")
                    ki.sendText(msg.to,"pornhub.com")
                    ki.sendText(msg.to,"anyporn.com")
                    ki.sendText(msg.to,"hdsexdino.com")
                    ki.sendText(msg.to,"rubyourdick.com")
                    ki.sendText(msg.to,"anybunny.mobi")
                    ki.sendText(msg.to,"cliphunter.com")
                    ki.sendText(msg.to,"sexloving.net")
                    ki.sendText(msg.to,"free.goshow.tv")
                    ki.sendText(msg.to,"eporner.com")
                    ki.sendText(msg.to,"Pornhd.josex.net")
                    ki.sendText(msg.to,"m.hqporner.com")
                    ki.sendText(msg.to,"m.spankbang.com")
                    ki.sendText(msg.to,"m.4tube.com")
                    ki.sendText(msg.to,"brazzers.com")
#----------------------------------------------------------
            elif "Bot?" in msg.text:
                ki.sendText(msg.to,"อะไรหรอครับ")
                ki2.sendText(msg.to,"ผมมาอยู่นานแล้ว....แหม่")
                ki3.sendText(msg.to,"กูว่ามึงพึ่งมานะ...!!!")
                ki4.sendText(msg.to,"ใช่หรอเพื่อนน")
                ki5.sendText(msg.to,"กูว่าพวกมึงถามผู้คุมดูนะ")
                ki6.sendText(msg.to,"ผู้คุมแม่งเงียบหวะ...")
                ki7.sendText(msg.to,"เอ่อๆๆมาก่อนมาหลังไม่สำคัญหรอกหำ")
                ki8.sendText(msg.to,"ขอแค่ยึดกลุ่มนี้ได้ก็พอมั้ง")
                ki9.sendText(msg.to,"เอ่อนั้นดิป่ะๆยึดแม่งหรือไม่ก็บินแม่ง")
                k1.sendText(msg.to,"Bot 💀10💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k2.sendText(msg.to,"Bot 💀11💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k3.sendText(msg.to,"Bot 💀12💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k4.sendText(msg.to,"Bot 💀13💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k5.sendText(msg.to,"Bot 💀14💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k6.sendText(msg.to,"Bot 💀15💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k7.sendText(msg.to,"Bot 💀16💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k8.sendText(msg.to,"Bot 💀17💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
                k9.sendText(msg.to,"Bot 💀18💀 •─ ͜͡✫ѕєʟғвот[ᴍ̶̲̅ᴀ̶̲̅ɴ̶̲̅]κɪcκєʀ ͜͡✫─•")
#---------------------------------
            elif msg.text in ["Test"]:
                ki.sendText(msg.to,"●")
                ki.sendText(msg.to,"●●")
                ki.sendText(msg.to,"●●●")
                ki.sendText(msg.to,"●●●●")
                ki.sendText(msg.to,"●●●●●")
                ki.sendText(msg.to,"●●●●●●")
                ki2.sendText(msg.to,"●●●●●●●")
                ki2.sendText(msg.to,"●●●●●●●●")
                ki2.sendText(msg.to,"●●●●●●●●●")
                ki2.sendText(msg.to,"●●●●●●●●●●")
                ki2.sendText(msg.to,"●●●●●●●●●●●")
                ki2.sendText(msg.to,"●●●●●●●●●●●●")
                ki3.sendText(msg.to,"●●●●●●●●●●●●●")
                ki3.sendText(msg.to,"●●●●●●●●●●●●●●")
                ki3.sendText(msg.to,"●●●●●●●●●●●●●●●")
                ki3.sendText(msg.to,"●●●●●●●●●●●●●●●●")
                ki3.sendText(msg.to,"●●●●●●●●●●●●●●●●●")
                ki3.sendText(msg.to,"●●●●●●●●●●●●●●●●●●")
                ki4.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●")
                ki4.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●")
                ki4.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●")
                ki4.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●")
                ki4.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●")
                ki4.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●")
                ki5.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●●")
                ki5.sendText(msg.to,"●●●●●●●●●●●●●●●●●●●●●●●●●●")
                ki5.sendText(msg.to,"●Bot Working●")
                cl.sendText(msg.to,"●( ^^)人(^^ )●")
#----------------------------------------------------
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + " Ngapain Ngetag?, ", cName + "Gw masih tidur,kalo ada perlu pc aja " + cName + "?", "Ada Perlu apa, " + cName + "?", "Apaan?", "Dont Tag Me!", cName + "Gak Usah Tag,Kalo Penting Pc aja!"]
                     ret_ = "[Auto Respond]\n" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendText(msg.to,ret_)

            elif 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    msg.contentType = 7
                    msg.text = None
                    msg.contentMetadata = {
                                         "STKID": "16846765",
                                         "STKPKGID": "8543",
                                         "STKVER": "7" }
                    for mention in mentionees:
                           if mention['M'] in admin:
                                  cl.sendMessage(msg)

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ngapain Ngetag?, ", cName + "Gw masih tidur,kalo ada perlu pc aja " + cName + "?", "Ada Perlu apa, " + cName + "?","Apaan?. ", "Dont Tag Me!"]
                     ret_ = "[Auto Respond]\n" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break
#-------------------------------------------------
            elif 'ยูทูป ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('ยูทูป ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
#-------------------------------------------------
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)	
#-------------------------------------------------
            elif msg.text.lower() == 'mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k1mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': k9mid}
                cl.sendMessage(msg)
		msg.contentMetadata = {'mid': w1mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': w9mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l1mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': l3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
#-------------------------------------------------
            elif "??¿ " in msg.text:
                       nk0 = msg.text.replace("??¿ ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                                    gs.preventJoinByTicket = True
                                    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                                    cl.updateGroup(gs)
#-----------------------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in admin:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait3["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki2.sendText(msg.to,"Fuck You")
                        ki3.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2,ki3,ki4,ki5,ki6]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#----------------------------------------
            elif msg.text in ["Kick on","kick on","Kickall","kickall","Kick all","kick all","Cleanse","cleanse","Nuke","nuke",".Kick on"]:
                    try:
                        cl.sendText(msg.to,"Mau ngapain?")
                        cl.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        pass

#----------------------------------------
            elif "รูป " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass
#========================================
            elif msg.text in ["Mypict"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
#----------------------------------------
            elif msg.text in ["Mycover"]:
                if msg.from_ in admin:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
#----------------------------------------
            elif "Hack @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Hack1 @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getvid @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendVideoWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
#----------------------------------------
            elif msg.text in ["Gu Tar","Kicker","หำ"]:
					G = cl.getGroup(msg.to)
					info = cl.getGroup(msg.to)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ticket = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k1.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k2.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k3.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k4.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k5.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k6.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k7.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k8.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					k9.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					w1.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					w2.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					w3.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					w4.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.01)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					cl.updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					cl.updateGroup(G)
#-----------------------------------------------------------                          
            elif msg.text in ["Gu bye","@bye","บาย"]:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     ki.leaveGroup(msg.to)
                     ki2.leaveGroup(msg.to)
                     ki3.leaveGroup(msg.to)
                     ki4.leaveGroup(msg.to)
                     ki5.leaveGroup(msg.to)
                     ki6.leaveGroup(msg.to)
                     ki7.leaveGroup(msg.to)
                     ki8.leaveGroup(msg.to)
                     ki9.leaveGroup(msg.to)
                     k1.leaveGroup(msg.to)
                     k2.leaveGroup(msg.to)
                     k3.leaveGroup(msg.to)
                     k4.leaveGroup(msg.to)
                     k5.leaveGroup(msg.to)
                     k6.leaveGroup(msg.to)
                     k7.leaveGroup(msg.to)
                     k8.leaveGroup(msg.to)
                     k9.leaveGroup(msg.to)
                except:
                     pass
#-----------------------------------------------------------      

            elif msg.text in ["Kill ban"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait3["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Fuck You By Min")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki2.kickoutFromGroup(msg.to,[jj])
                        ki3.kickoutFromGroup(msg.to,[jj])
                        ki4.kickoutFromGroup(msg.to,[jj])
                        ki5.kickoutFromGroup(msg.to,[jj])
                        ki6.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Good Bye")                                              
#-------------------------------------------------
            elif ("แบน " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait3["blacklist"][target] = True
                      with open('bl.json', 'w') as fp:
                           json.dump(wait3, fp, sort_keys=True, indent=4)
                      cl.sendText(msg.to,"Succes ครับ")
                   except:
                      pass
#-------------------------------------------------

#-------------------------------------------------

#-------------------------------------------------

#-------------------------------------------------
            elif "Phet Keyy" in msg.text:
                cl.sendText(msg.to,""" 􀜁􀇔􏿿􀜁􀇔􏿿[{PHET HACK BOT}] 􀜁􀇔􏿿􀜁􀇔􏿿 \n\n 􀜁􀇔􏿿 key Only Kicker 􀜁􀇔􏿿 \n\n􀜁􀇔􏿿[Kb1 in]\n􀜁􀇔􏿿[1Aditname:]\n􀜁􀇔􏿿[B Cancel]\n􀜁􀇔􏿿[kick @]\n􀜁􀇔􏿿[Ban @]\n􀜁􀇔􏿿[kill]\n􀜁􀇔􏿿[BotChat]\n􀜁􀇔􏿿[Respons]\n􀜁􀇔􏿿[Pb1 Gift]\n􀜁􀇔􏿿[Pb1 bye]\n\n

❦❧〖฿❂Ŧ〗☞ᵀËÄM ທஇລ❂ق B❂T✓
​❦❧ ᵀËÄM ℓℓπ้ी૪ B❂T ✓
❦❧ ᵀËÄM ທஇລ❂قB❂T ✓
☠Ҝŋ β☢ȶȶ ƿℓαÿєᴿ☠
✍ Ŧ€₳M ж Ħ₳ʗҜ฿❂Ŧ ✈​
Ŧ€₳M ​✍ ທஇລ❂قীள้௭ิњ ✈
☢Ŧ€₳M≈ನန้ণএ≈฿❂Ŧ☢
･⋆ ざঝণのঝ  ⋆ ･
♤ のю४ণধபӘທ ♤
🇹🇭 ฿ΘŧŧĽÎη℮Ŧђάίłάήđ 🇹🇭

[By.🐯 हईທຮຮๅજईह 🐯]
[By.β•`BF.บั้ม•`]
[By.Gυ Tєʌм HʌcκBoт]
[By.❦〖Ᵽɧëȶ〗☞ᵀËÄM ທஇລ❂ق B❂T✓]
""")

#-------------------------------------------------
            elif "#v10" in msg.text:
                cl.sendText(msg.to,"""[SELFBOT PHET HACK BOT]\n\n
Phet Tema Hack Bot
คำสั่งบอท siri
คำนี้เป็นการล็อกห้องสั่งแล้วทุกคนจะทำอะไรไม่ได้นอกจากเจ้าของห้องทำได้คนเดียวเช่น•เปิดลิงค์•เชิญเพื่อน•เปลี่ยนรูปกลุ่ม•เปลี่ยนชื่อกลุ่มไรแบบนี้• บอทจะไม่เตะเเอทมินทุกกรณี
มีตั้งเเต่ชุดบอท 12-37 บอท
ชุดล๊อกห้อง
ล๊อกกันรันสติ๊กเกอร์
Set:StampLimitation:on

ล๊อกชื่อกลุ่ม
Set:changenamelock:on

ล๊อกการเชิญของสมาชิก
Set:blockinvite:on

ล๊อกแอทมินกลุ่ม
Set:ownerlock:on

ล๊อกรูปกลุ่ม
Set:iconlock:on

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeowner
เปลี่ยนเจ้าของห้องสั่งแล้วส่งคอลแทคคนที่จะเป็นเจ้าของห้องคนต่อไปลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addblacklist
บัญชีดำแบ็คลิสคนไม่ให้เข้ากลุ่มสั่งแล้วส่งคอลแทคคนที่เราจะแบ็คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:addwhitelist
บัญชีขาวแก้ดำสั่งแล้วส่งคอลแทคคนที่เราจะแก้แบ๊คลิสลงในกลุ่ม
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:blockinvite:off  ปลดล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Set:blockinvite:on  ล็อกการเชิญ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:inviteurl         เปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:DenyURLInvite  ปิดลิงค์
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:cancelinvite  ยกเลิกค้างเชิญสั่ง2ครั้ง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:groupcreator เช็คเจ้าของบ้านตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
Siri:extracreator  เช็คเจ้าของบ้านคนสำรอง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

set:changeextraowner 
เพิ่มเจ้าของบ้านคนที2หรือเรียกคนสำรองสั่งแล้วส่งคอลแทคคนที่จะเป็นคนสำรองลงในกลุ่ม

➖➖➖➖➖➖➖➖➖➖➖➖➖➖

Set:turncreator

สลับให้เจ้าของบ้านคนที่2เป็นตัวจริง
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

ดูคนอ่าน

สั่งตั้งค่าก่อนแล้วค่อยสั่งอ่านคน

Setlastpoint     ตั้งค่า

Viewlastseen   สั่งอ่าน
➖➖➖➖➖➖➖➖➖➖➖➖➖➖

สนใจติดต่อที่
http://line.me/ti/p/socool290
เพชรทีมทดลองบอท
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
""")

#-------------------------------------------------
            elif msg.text in ["Notifed on","เปิดแจ้งเตือน","M on"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดการแจ้งเตือนแล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดการแจ้งเตือนแล้ว")
                else:
                    wait["Notifed"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"เปิดการแจ้งเตือนแล้ว")
                    else:
                        cl.sendText(msg.to,"เปิดการแจ้งเตือนแล้ว")
            elif msg.text in ["Notifed off","ปิดแจ้งเตือน","M off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดการแจ้งเตือนแล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดการแจ้งเตือนแล้ว")
                else:
                    wait["Notifed"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปิดการแจ้งเตือนแล้ว")
                    else:
                        cl.sendText(msg.to,"ปิดการแจ้งเตือนแล้ว")

            elif msg.text in ["Notifedbot on","เปิดเเจ้งเตือนบอท","Mbot on"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
            elif msg.text in ["Notifedbot off","ปิดแจ้งเตือนบอท","Mbot off"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        cl.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")
#-----------------------------------------------
        if op.type == 15:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nเเล้วพบใหม่นะ")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nยินดีต้อนรับสู่ "+ str(ginfo.name))
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nไม่น่าจะจุกเท่าไหร่หรอก")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\nเเล้วพบใหม่นะ")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\nเเล้วพบใหม่นะ")
                print "MEMBER OUT GROUP"


        if op.type == 17:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\nเเล้วพบใหม่นะ")

                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 19:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\nไม่น่าจะจุกเท่าไหร่หรอก")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\nไม่น่าจะจุกเท่าไหร่หรอก")
                print "MEMBER HAS KICKOUT FROM THE GROUP"


                    
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------
            elif msg.text in ["Bot Sp","Bot speed"]:
                start = time.time()
                ki.sendText(msg.to, "Mohon Bersabar Ini Gratisan...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
                ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
                elapsed_time = time.time() - start
            
            elif msg.text.lower() == 'responsname':
                profile = ki.getProfile()
                text = profile.displayName
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName
                ki4.sendText(msg.to, text)

#------------------------------------------------------------------	
            elif "/มอง @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("/มอง @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
 #------------------------------------------------------------------
            elif "Bl @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Bl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"Error")
                                
            elif "Bl all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Bl all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Hapus")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Success Boss")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")
            
            elif "Wl @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Wl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")

            elif "Blacklist:" in msg.text:       
             if msg.from_ in admin:           
                       nk0 = msg.text.replace("Blacklist:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Whitelist:" in msg.text:             
              if msg.from_ in admin:     
                       nk0 = msg.text.replace("Whitelist:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif msg.text in ["Ban on"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"clear")
            elif msg.text in ["Whitelist","ยัดดำ","Ban contact"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Blacklist","เเก้ดำ","Unban contact"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["เชคดำ","Mcheck"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing 􀨁􀄻double thumbs up􏿿")
                else:
                    cl.sendText(msg.to,"Daftar Banlist􏿿")
                    mc = "[⎈]Blacklist [⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
            elif msg.text in ["Ban cek","Meban","Mcheck mid"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text.lower() == 'kill':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            ki6.kickoutFromGroup(msg.to,[jj])
                            ki7.kickoutFromGroup(msg.to,[jj])
                            ki8.kickoutFromGroup(msg.to,[jj])
                            ki9.kickoutFromGroup(msg.to,[jj])
                            k1.kickoutFromGroup(msg.to,[jj])
                            k2.kickoutFromGroup(msg.to,[jj])
                            k3.kickoutFromGroup(msg.to,[jj])
                            k4.kickoutFromGroup(msg.to,[jj])
                            k5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "!NK" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("!NK","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = w1.getGroup(msg.to)
                    gs = w2.getGroup(msg.to)
                    gs = w3.getGroup(msg.to)
                    gs = w4.getGroup(msg.to)
                    gs = w5.getGroup(msg.to)
                    cl.sendText(msg.to,"Masih Mauko Sundala")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak ada Member")
                        ki2.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,w1,w2,w3]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Hahaha")
                                ki2.sendText(msg,to,"Fakyu Sundala")

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == ["Botjoin ps1","มาหำ","Go go"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text in ["#Phet","#phet","Botjoin sp2","•••"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        w9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        l3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
#                        l4.acceptGroupInvitationByTicket(msg.to,Ticket)
#                        time.sleep(0.01)
#                        l5.acceptGroupInvitationByTicket(msg.to,Ticket)
#                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == '••':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        w2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Pb1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Pro2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Pro3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Pro4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Pro5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Pro6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "Pro7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "Pro8 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "Pro9 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "Pro10 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k1.updateGroup(G)
#-----------------------------------------------
            elif "Pro11 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k2.updateGroup(G)
#-----------------------------------------------
            elif "Pro12 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k3.updateGroup(G)
#-----------------------------------------------
            elif "Pro13 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k4.updateGroup(G)
#-----------------------------------------------
            elif "Pro14 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k5.updateGroup(G)
#-----------------------------------------------
            elif "Pro15 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k6.updateGroup(G)
#-----------------------------------------------
            elif "Pro16 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.gtGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k7.updateGroup(G)
#-----------------------------------------------
            elif "Pro17 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k8.updateGroup(G)
#-----------------------------------------------
            elif "Pro18 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        k9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        k9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        k9.updateGroup(G)
#-----------------------------------------------
            elif "Pro19 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        w1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        w1.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        w1.updateGroup(G)
#-----------------------------------------------
            elif "Botl3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        l3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        l3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        l3.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["บายหำ","#Bye","#bye","•"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Bye~Bye"  +  str(ginfo.name)  + "\n\n[By.เพชร ทีมทดลองบอท]")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                        k4.leaveGroup(msg.to)
                        k5.leaveGroup(msg.to)
                        k6.leaveGroup(msg.to)
                        k7.leaveGroup(msg.to)
                        k8.leaveGroup(msg.to)
                        k9.leaveGroup(msg.to)
                        w1.leaveGroup(msg.to)
                        w2.leaveGroup(msg.to)
                        w3.leaveGroup(msg.to)
                        w4.leaveGroup(msg.to)
                        w5.leaveGroup(msg.to)
                        w6.leaveGroup(msg.to)
                        w7.leaveGroup(msg.to)
                        w8.leaveGroup(msg.to)
                        w9.leaveGroup(msg.to)
                        l1.leaveGroup(msg.to)
                        l2.leaveGroup(msg.to)
                        l3.leaveGroup(msg.to)
#                        l4.leaveGroup(msg.to)
#                        l5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Po6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P11 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P12 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P13 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P14 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P15 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P16 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P17 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P18 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        k9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P19 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        w1.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "P20 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        w2.leaveGroup(msg.to)
                    except:
                        pass

            elif msg.text in ["Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        #l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       #l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                       # l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                      #  l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                      #  l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

            	elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l4.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l4.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
          #              l4.acceptGroupInvitationByTicket(op.param1,Ticket)
           #             l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l4.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l4.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l4.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in k1mid:
                        G = k1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)
                    else:
                        G = k1.getGroup(op.param1)

                        
                        k1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k1.updateGroup(G)

                elif op.param3 in k1mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l4.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k2mid:
                        G = k2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)
                    else:
                        G = k2.getGroup(op.param1)

                        
                        k2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k2.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k3mid:
                        G = k3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l4.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)
                    else:
                        G = k3.getGroup(op.param1)

                        
                        k3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k3.updateGroup(G)

                elif op.param3 in k3mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in k4mid:
                        G = k4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)
                    else:
                        G = k4.getGroup(op.param1)

                        
                        k4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l4.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k4.updateGroup(G)

                elif op.param3 in k4mid:
                    if op.param2 in k5mid:
                        G = k5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l4.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)
                    else:
                        G = k5.getGroup(op.param1)

                        
                        k5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k5.updateGroup(G)

                elif op.param3 in k5mid:
                    if op.param2 in k6mid:
                        G = k6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k6.updateGroup(G)
                        Ticket = k6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
           #             l4.acceptGroupInvitationByTicket(op.param1,Ticket)
          #              l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k6.updateGroup(G)
                    else:
                        G = k6.getGroup(op.param1)

                        
                        k6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k6.updateGroup(G)
                        Ticket = k6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
             #           l4.acceptGroupInvitationByTicket(op.param1,Ticket)
            #            l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k6.updateGroup(G)

                elif op.param3 in k6mid:
                    if op.param2 in k7mid:
                        G = k7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k7.updateGroup(G)
                        Ticket = k7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k7.updateGroup(G)
                    else:
                        G = k7.getGroup(op.param1)

                        
                        k7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k7.updateGroup(G)
                        Ticket = k7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k7.updateGroup(G)

                elif op.param3 in k7mid:
                    if op.param2 in k8mid:
                        G = k8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k8.updateGroup(G)
                        Ticket = k8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k8.updateGroup(G)
                    else:
                        G = k8.getGroup(op.param1)

                        
                        k8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k8.updateGroup(G)
                        Ticket = k8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k8.updateGroup(G)

                elif op.param3 in k8mid:
                    if op.param2 in k9mid:
                        G = k9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        k9.updateGroup(G)
                        Ticket = k9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l4.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k9.updateGroup(G)
                    else:
                        G = k9.getGroup(op.param1)

                        
                        k9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        k9.updateGroup(G)
                        Ticket = k9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l4.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        k9.updateGroup(G)

                elif op.param3 in k9mid:
                    if op.param2 in w1mid:
                        G = w1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w1.updateGroup(G)
                        Ticket = w1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                  l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w1.updateGroup(G)
                    else:
                        G = w1.getGroup(op.param1)

                        
                        w1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w1.updateGroup(G)
                        Ticket = w1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l4.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w1.updateGroup(G)

                elif op.param3 in w1mid:
                    if op.param2 in w2mid:
                        G = w2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w2.updateGroup(G)
                        Ticket = w2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l4.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w2.updateGroup(G)
                    else:
                        G = w2.getGroup(op.param1)

                        
                        w2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w2.updateGroup(G)
                        Ticket = w2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w2.updateGroup(G)
                        
                elif op.param3 in w2mid:
                    if op.param2 in w3mid:
                        G = w3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w3.updateGroup(G)
                        Ticket = w3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w3.updateGroup(G)
                    else:
                        G = w3.getGroup(op.param1)

                        
                        w3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w3.updateGroup(G)
                        Ticket = w3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w3.updateGroup(G)
                        
                elif op.param3 in w3mid:
                    if op.param2 in w4mid:
                        G = w4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w4.updateGroup(G)
                        Ticket = w4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w4.updateGroup(G)
                    else:
                        G = w4.getGroup(op.param1)

                        
                        w4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w4.updateGroup(G)
                        Ticket = w4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w4.updateGroup(G)
                        
                elif op.param3 in w4mid:
                    if op.param2 in w5mid:
                        G = w5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w5.updateGroup(G)
                        Ticket = w5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w5.updateGroup(G)
                    else:
                        G = w5.getGroup(op.param1)

                        
                        w5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w5.updateGroup(G)
                        Ticket = w5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w5.updateGroup(G)
                        
                elif op.param3 in w5mid:
                    if op.param2 in w6mid:
                        G = w6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w6.updateGroup(G)
                        Ticket = w6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
          #              l4.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w6.updateGroup(G)
                    else:
                        G = w6.getGroup(op.param1)

                        
                        w6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w6.updateGroup(G)
                        Ticket = w6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
           #             l4.acceptGroupInvitationByTicket(op.param1,Ticket)
            #            l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w6.updateGroup(G)
                        
                elif op.param3 in w6mid:
                    if op.param2 in w7mid:
                        G = w7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w7.updateGroup(G)
                        Ticket = w7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
             #           l4.acceptGroupInvitationByTicket(op.param1,Ticket)
              #          l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w7.updateGroup(G)
                    else:
                        G = w7.getGroup(op.param1)

                        
                        w7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w7.updateGroup(G)
                        Ticket = w7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
#                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
 #                       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w7.updateGroup(G)
                        
                elif op.param3 in w7mid:
                    if op.param2 in w8mid:
                        G = w8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w8.updateGroup(G)
                        Ticket = w8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
   #                     l4.acceptGroupInvitationByTicket(op.param1,Ticket)
  #                      l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w8.updateGroup(G)
                    else:
                        G = w8.getGroup(op.param1)

                        
                        w8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w8.updateGroup(G)
                        Ticket = w8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
    #                    l4.acceptGroupInvitationByTicket(op.param1,Ticket)
     #                   l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w8.updateGroup(G)
                        
                elif op.param3 in w8mid:
                    if op.param2 in w9mid:
                        G = w9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        w9.updateGroup(G)
                        Ticket = w9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
       #                 l4.acceptGroupInvitationByTicket(op.param1,Ticket)
      #                  l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w9.updateGroup(G)
                    else:
                        G = w9.getGroup(op.param1)

                        
                        w9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        w9.updateGroup(G)
                        Ticket = w9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
        #                l4.acceptGroupInvitationByTicket(op.param1,Ticket)
         #               l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        w9.updateGroup(G)
                        
                elif op.param3 in w9mid:
                    if op.param2 in l1mid:
                        G = l1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l1.updateGroup(G)
                        Ticket = l1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
           #             l4.acceptGroupInvitationByTicket(op.param1,Ticket)
          #              l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l1.updateGroup(G)
                    else:
                        G = l1.getGroup(op.param1)

                        
                        l1.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l1.updateGroup(G)
                        Ticket = l1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
             #           l4.acceptGroupInvitationByTicket(op.param1,Ticket)
            #            l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l1.updateGroup(G)
                        
                elif op.param3 in l1mid:
                    if op.param2 in l2mid:
                        G = l2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l2.updateGroup(G)
                        Ticket = l2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
              #          l4.acceptGroupInvitationByTicket(op.param1,Ticket)
              #          l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l2.updateGroup(G)
                    else:
                        G = l2.getGroup(op.param1)

                        
                        l2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l2.updateGroup(G)
                        Ticket = l2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                #        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
               #         l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l2.updateGroup(G)
                        
                elif op.param3 in l2mid:
                    if op.param2 in l3mid:
                        G = l3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l3.updateGroup(G)
                        Ticket = l3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                 #       l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                 #       l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l3.updateGroup(G)
                    else:
                        G = l3.getGroup(op.param1)

                        
                        l3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l3.updateGroup(G)
                        Ticket = l3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  #      l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                   #     l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l3.updateGroup(G)
                        
 #               elif op.param3 in l3mid:
  #                  if op.param2 in l4mid:
   #                     G = l4.getGroup(op.param1)
    #                    G.preventJoinByTicket = False
     #                   l4.updateGroup(G)
                        Ticket = l4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l4.updateGroup(G)
      #              else:
                        G = l4.getGroup(op.param1)

                        
                        l4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l4.updateGroup(G)
                        Ticket = l4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l4.updateGroup(G)
                        
       #         elif op.param3 in l4mid:
#                    if op.param2 in l5mid:
#                        G = l5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        l5.updateGroup(G)
                        Ticket = l5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        l5.updateGroup(G)
 #                   else:
                        G = l5.getGroup(op.param1)

                        
                        l5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        l5.updateGroup(G)
                        Ticket = l5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        w9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        l5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
  #                      l5.updateGroup(G)
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	    else:
		cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	    else:
		cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	    else:
		cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
	    else:
		cl.sendText(op.param1,"You update the group.\n\n[By.เพชร ทีมทดลองบอท]")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    random.choice(KAC).updateGroup(G)
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n✪ " + Nama
                        wait2['ROM'][op.param1][op.param2] = "✪ " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"༺%H:%M༻")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

def autolike():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   ki9.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k3.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k4.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k5.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k6.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k7.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k8.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   k9.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   w1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
#                   w2.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki6.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki7.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki8.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          ki9.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k3.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k4.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k5.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k6.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k7.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k8.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          k9.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          w1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
#                          w2.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

#def autolike():
#     for zx in range(0,50):
#        hasil = cl.activity(limit=1000)
#        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#          try:    
#            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki3.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki3.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki4.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki4.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki5.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki5.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            ki6.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#            ki6.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by MuhMursalinD\n\nHttp://line.me/ti/p/~muhmursalind")
#            print "Like"
#            print "Like"
#            print "Like"
#          except:
#            pass
#        else:
#            print "Already Liked"
#     time.sleep(600)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
