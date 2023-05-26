from PIL import Image, ImageDraw

im1 = Image.open('quadro0000.png').convert('P')
im2 = Image.open('quadro0001.png').convert('P')
im3 = Image.open('quadro0002.png').convert('P')
im4 = Image.open('quadro0003.png').convert('P')
im5 = Image.open('quadro0004.png').convert('P')
im6 = Image.open('quadro0005.png').convert('P')
im7 = Image.open('quadro0006.png').convert('P')
im8 = Image.open('quadro0007.png').convert('P')
im9 = Image.open('quadro0008.png').convert('P')
im10 = Image.open('quadro0009.png').convert('P')
im11 = Image.open('quadro0010.png').convert('P')
im12 = Image.open('quadro0011.png').convert('P')
im13 = Image.open('quadro0012.png').convert('P')
im14 = Image.open('quadro0013.png').convert('P')
im15 = Image.open('quadro0014.png').convert('P')


im1.save('output2.gif', save_all=True, append_images=[im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11, im12, im13, im14, im15], loop=0, duration=20, transparency=255, disposal=2)