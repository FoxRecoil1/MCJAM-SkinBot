from PIL import Image, ImageEnhance
import os
import discord
from discord.ext import commands
token = str(input("Введите токен бота:"))
prefix = str(input("Введите префикс бота (/, ! и т.д):"))
commands = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@commands.command()
async def AmethystSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Amethyst/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def AmethystAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Amethyst/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def AdminSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Admin/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def AdminAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Admin/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def AmberSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Amber/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def AmberAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Amber/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def DiamondSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Diamond/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def DiamondAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Diamond/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def EmeraldSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Emerald/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def EmeraldAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Emerald/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def LapizSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Lapiz/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def LapizAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Lapiz/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def RubySteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Ruby/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def RubyAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Ruby/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def SapphireSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Sapphire/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def SapphireAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Sapphire/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def TopazSteve(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Topaz/Steve.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')
@commands.command()
async def TopazAlex(ctx):
    if len(ctx.message.attachments) > 0:
      for attach in ctx.message.attachments:
          filename1 = f'skin_{ctx.author.id}_{attach.id}.png'
          imgn = attach.filename
          await attach.save(filename1)
          Color = Image.open(r"Asset/Topaz/Alex.png")
          PlayerSkin = Image.open(filename1)
          PlayerSkin = PlayerSkin.convert("RGBA")
          EtnosPixel = (8, 15, 9, 16)
          SkinHead = (0, 0, 64, 16)
          SkinCropHead = PlayerSkin.crop(SkinHead)
          EtnosPixelCrop = PlayerSkin.crop(EtnosPixel)
          Color.paste(SkinCropHead, (0, 0), mask=SkinCropHead)
          Color.paste(EtnosPixelCrop, (23, 20), mask=EtnosPixelCrop)
          enhancer = ImageEnhance.Brightness(EtnosPixelCrop)
          EtnosPixelCrop1 = enhancer.enhance(0.95)
          Color.paste(EtnosPixelCrop1, (24, 20), mask=EtnosPixelCrop1)
          Color.save(filename1)
          await ctx.send(file=discord.File(filename1))
          os.remove(filename1)
    else:
        await ctx.send('Отправьте изображение, пожалуйста.')


commands.run(token)