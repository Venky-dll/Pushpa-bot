from discord.ext import commands
import cmath

@commands.command(name='roots')
async def roots(ctx, a, b, c):
    
    a, b, c = float(a), float(b), float(c)
        
    if a == 0 and c == 0:
        await ctx.send(f'The root is: 0 ,not worth asking')

    elif a == 0 and b == 0:
        await ctx.send(f'That makes no sense :point_up: :nerd:')

    elif a == 0:
        root = float(-c/b)
        await ctx.send(f'The equation is linear and the root is: ({root})')

        
    else:
         # Calculate the discriminant
         dis = (b ** 2) - (4 * a * c)

         # Calculate the roots
         root1 = (-b - cmath.sqrt(dis)) / (2 * a)
         root2 = (-b + cmath.sqrt(dis)) / (2 * a)

         # Send the roots as a response
         await ctx.send(f'The roots are: {root1}, {root2}')

    
