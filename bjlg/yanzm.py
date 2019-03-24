# from django.http import HttpResponse
#
#
# def verifycode(request):
#     # 引入绘图模块
#     from PIL import Image, ImageDraw, ImageFont
#     # 引入随机函数模块
#     import random
#     # 定义变量,用于画面的背景色,长宽高
#     bgcolor = (random.randrange(20, 100), random.randrange(20, 100), random.randrange(20, 100))
#     width = 100
#     height = 50
#     # 创建画面对象
#     im = Image.new('RGB', (width, height), bgcolor)
#     # 创建画笔对象
#     draw = ImageDraw.Draw(im)
#     for i in range(0, 100):
#         xy = (random.randrange(0, width), random.randrange(0, height))
#         fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
#         draw.point(xy, fill=fill)
#         # 定义验证码的被选值
#     str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
#     rand_str = ''
#     for i in range(0, 4):
#         rand_str += str[random.randrange(0, len(str))]
#     # 构造字体对象
#     font = ImageFont.truetype(r'/Applications/Font Book.app/Contents/Resources/Base.lproj/FBFontsView.nib', 40)
#     # 构造字体颜色
#     fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
#     fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
#     fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
#     fontcolor4 = (255, random.randrange(0, 255), random.randrange(0, 255))
#
#     draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
#     draw.text((25, 2), rand_str[1], font=font, fill=fontcolor2)
#     draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
#     draw.text((75, 2), rand_str[3], font=font, fill=fontcolor4)
#     # 释放画笔
#     del draw
#     request.session['verifycode'] = rand_str
#     import io
#
#     buf = io.BytesIO()
#     # 将图片保存起来给浏览器
#     im.save(buf, 'png')
#     # 将内存的图片数据给客户端
#     return HttpResponse(buf.getvalue(), 'image/png')
#
#
# from django.shortcuts import render, redirect
#
#
# def verifycodefile(request):
#     f = request.session["falg"]
#
#     str = ""
#     if f == False:
#         str = "􏶃􏴚􏲕􏲮􏰾􏴼"
#     request.session.clear()
#     return render(request, 'myApp/verifycodefile.html', {"flag": str})
#
#
# def verifycodecheck(request):
#     code1 = request.POST.get("verifycode").upper()
#     code2 = request.session["verify"].upper()
#     if code1 == code2:
#
#         return render(request, 'myApp/success.html')
#     else:
#         request.session["flag"] = False
#         return redirect('/verifycodefile')
