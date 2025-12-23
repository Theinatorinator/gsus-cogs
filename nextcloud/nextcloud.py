from io import BytesIO

from tsutils.cogs.apicog import CogWithEndpoints, endpoint

class NextCloud(CogWithEndpoints):
    GSUS_SERVER_ID = 1054471846436798535

    """A cog to interface with NextCloud."""
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    async def red_get_data_for_user(self, *, user_id):
        """Get a user's personal data."""
        data = "No data is stored for user with ID {}.\n".format(user_id)
        return {"user_data.txt": BytesIO(data.encode())}

    async def red_delete_data_for_user(self, *, requester, user_id):
        """Delete a user's personal data.

        No personal data is stored in this cog.
        """
        return

    @endpoint("user_info")
    async def user_info(self, user_id: int):
        """Get info about a user."""
        member = await self.bot.get_guild(self.GSUS_SERVER_ID).fetch_member(user_id)
        if member is None:
            return {
                'response': {'error': 'Member not in GSUS server.'},
                'status': 404
            }

        return {
                'response': {
                    'avatar_url': member.avatar.url if member.avatar else None,
                    'name': member.name,
                    'account_creation': member.created_at.timestamp(),
                    'roles': [role.id for role in member.roles],
                },
                'status': 404
            }



