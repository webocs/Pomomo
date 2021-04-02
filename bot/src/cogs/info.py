from discord.ext import commands
from utils import msg_builder
import user_messages as u_msg
from session import session_manager
from random import choice


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, command=''):
        help_embed = msg_builder.help_embed(command)
        if help_embed:
            await ctx.send(embed=help_embed)
        else:
            await ctx.send('Enter a valid command.')

    @commands.command()
    async def time(self, ctx):
        session = await session_manager.get_server_session(ctx)
        if session:
            await ctx.send(f'{session.timer.time_remaining_to_str()} remaining on {session.state}!')

    @commands.command()
    async def settings(self, ctx):
        session = await session_manager.get_server_session(ctx)
        if session:
            await ctx.send(embed=msg_builder.settings_embed(session.settings))

    @commands.command()
    async def stats(self, ctx):
        session = await session_manager.get_server_session(ctx)
        if session:
            stats = session.stats
            if stats.pomos_completed > 0:
                await ctx.send(f'You\'ve completed {msg_builder.stats_msg(stats)} so far. ' +
                               choice(u_msg.ENCOURAGEMENTS))
            else:
                await ctx.send('You haven\'t completed any pomodoros yet.')


def setup(client):
    client.add_cog(Info(client))
