
from report import models
from report.models import announcement, schedule, user, check_day, sys_dd_item

def get_value():
    user_name_tuple = models.user.objects.filter(user_type=1,user_group_role=1)
    for i in range(len(user_name_tuple)):
        dex = user_name_tuple[i].user_name
        source_tuple1=tuple()
        source_tuple2=tuple(dex,dex)
        target_tuple=target_tuple+source_tuple2
