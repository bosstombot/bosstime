async def bunbae_(ctx):
		if ctx.message.channel.id == basicSetting[7]:
			msg = ctx.message.content[len(ctx.invoked_with)+1:]
			separate_money = []
			separate_money = msg.split(" ")
			num_sep = floor(int(separate_money[0]))
			cal_tax1 = floor(float(separate_money[1])*0.05)
			
			real_money = floor(floor(float(separate_money[1])) - cal_tax1)
			cal_tax2 = floor(real_money*0.05)
			if num_sep == 0 :
				await ctx.send('```분배 인원이 0입니다. 재입력 해주세요.```', tts=False)
			else :
				embed = discord.Embed(
					title = "----- 분배결과! -----",
					description= '```세금 : ' + str(cal_tax1) + '\n수령액 : ' + str(real_money) + '\n혈비 : ' + str(cal_tax2) + '\n인당수령액 : ' + str(floor(float(floor(real_money/num_sep))*0.9)) + '```',
					color=0xff00ff
					)
				await ctx.send(embed=embed, tts=False)
		else:
			return
