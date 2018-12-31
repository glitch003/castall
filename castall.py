import pychromecast

print("Getting chromecasts")
chromecasts = pychromecast.get_chromecasts()
# repub debate
url = 'https://s3-us-west-1.amazonaws.com/chriscassano-dev/hendrix.mp4'

# loose change
# url = 'https://redirector.googlevideo.com/videoplayback?ei=QDbAWvL7FsGv4QTHj5jwBw&c=WEB&lmt=1507262093330097&expire=1522567840&ratebypass=yes&ipbits=0&sparams=dur%2Cei%2Cid%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&dur=4215.814&requiressl=yes&id=o-AGyejnvhXMzxYIArplTo2ZmY_FyVBsydZmnOXpgztPJX&pl=27&mn=sn-hp57yne6%2Csn-5uaeznyz&mm=31%2C26&itag=22&ms=au%2Conr&mv=u&mt=1522545874&fvip=5&source=youtube&key=yt6&mime=video%2Fmp4&ip=104.156.245.194&signature=355A917243EF52931F265A22019E8B88F5E1B63F.1CEEBA9E79A28633284791AF56D041450B3AA753&title=LOOSE+CHANGE+2ND+EDITION+%282005%29+HD+OFFICIAL&title=LOOSE+CHANGE+2ND+EDITION+%282005%29+HD+OFFICIAL'

# kennedy doc
# url = 'https://redirector.googlevideo.com/videoplayback?sparams=dur%2Cei%2Cid%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&ipbits=0&mm=31%2C26&ratebypass=yes&mn=sn-ab5l6nsr%2Csn-tt1e7nel&mime=video%2Fmp4&id=o-AB476iBKtC8JrmO3DvaslYZb9g9Vx8pVEZJ1jiePMjRi&pl=25&source=youtube&mv=u&ms=au%2Conr&ip=207.246.81.208&requiressl=yes&c=WEB&ei=KmTAWvbqJIu98wTl8o6ICQ&mt=1522556030&signature=14F6412DECBDE274CBE95A87AB5D1DC70EFED1D6.DD496F46E86EDAAE0944FC5328D51B0E8BC27C23&dur=4580.275&fvip=5&key=yt6&lmt=1520213849046892&itag=22&expire=1522579594&title=JFK+Assassination+Questions+that+Just+Won%27t+go+Away+DOCUMENTARY&title=JFK+Assassination+Questions+that+Just+Won%27t+go+Away+DOCUMENTARY'

# reptile doc
# url = 'https://redirector.googlevideo.com/videoplayback?mn=sn-ab5l6ndr%2Csn-ab5sznle&expire=1522587740&mm=31%2C29&ipbits=0&ip=207.246.126.103&key=yt6&lmt=1508881306223057&dur=2805.899&mv=u&pl=27&mt=1522565895&ms=au%2Crdu&ei=_IPAWpm3Dpa2hwaZ_7A4&signature=8BF06998C023DDC4EC918525B879D54D0BF97F37.1199F9C415FAA831EA70799B618CD8E6476993&source=youtube&sparams=dur%2Cei%2Cid%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&fvip=3&c=WEB&mime=video%2Fmp4&id=o-AOxROgZF1Mm_Ida-QvqcXN3_MkaVUymaTfEpDN0EiBGf&itag=22&ratebypass=yes&requiressl=yes&title=Diana%3A+The+Witnesses+In+The+Tunnel+%28Conspiracy+Theory+Documentary%29+-+Real+Stories&title=Diana%3A+The+Witnesses+In+The+Tunnel+%28Conspiracy+Theory+Documentary%29+-+Real+Stories'

print("Got em.  Looping over {} chromecasts: ".format(len(chromecasts)))
print([cc.device.friendly_name for cc in chromecasts])

for cc in chromecasts:
  print("-------------------------------")
  print("-------------------------------")
  print("Getting info on {}".format(cc.device.friendly_name))
  cc.wait()
  print(cc.device)
  print(cc.status)

  if cc.device.cast_type == 'audio':
    print("Device is audio only.  Skipping.")
    continue # skip audio

  # cast to device

  # remove to cast all devices
  # cc.device.friendly_name == "Not Your TV"
  # if cc.device.friendly_name == "Brooks was here TV" or cc.device.friendly_name == "Naphtastic Chromecastic":
    # continue

  print("***** Casting to {} *****".format(cc.device.friendly_name))
  mc = cc.media_controller
  mc.play_media(url, 'video/mp4')
  mc.block_until_active()
  print(mc.status)
  print(cc.device)
  print(cc.status)