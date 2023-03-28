from django.utils.translation import ugettext_noop
from lms.djangoapps.courseware.tabs import EnrolledTab

class GraspwayChatTab(EnrolledTab):
    """
    The representation of the course teams view type.
    """
    type = "gwchat"
    name = "gwchat"
    title = ugettext_noop("Chat")
    view_name = "gwchat"
    is_default = True
    tab_id = "gwchat"
    is_hideable = True
    view_name = "gwchat_view"

    @classmethod
    def is_enabled(cls, course, user=None):
        """Returns true if gw-chat  is enabled in the course.
        Args:
            course (CourseDescriptor): the course using the feature
            user (User): the user interacting with the course
        """
        if not super(GraspwayChatTab, cls).is_enabled(course, user=user):
            return False

#        if not settings.FEATURES.get("GW_CHAT_TAB_ENABLED"):
#            return False

        if user and not user.is_authenticated:
            return False

        return True
# settings.FEATURES.get('GW_CHAT_TAB_ENABLED', True)
