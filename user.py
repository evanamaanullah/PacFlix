from dataclasses import dataclass
from datetime import datetime
from dateutil import relativedelta
from plan import Plan

@dataclass
class User:
  username: str
  plan: Plan
  start_subs_time: datetime
  referral_code: str=None

  def __post_init__(self):
    self.invoice = self.plan.price

  def upgrade_plan(self, new_plan):
    #check if not downgrade
    if new_plan.level < self.plan.level:
      print('Plan tidak boleh downgrade')
      return

    #if start subs time > 12 months, add 5% discount
    discount = 1
    difference = relativedelta.relativedelta(datetime.now(), self.start_subs_time)
    print(difference.years)
    if difference.years > 1:
      discount = 0.95

    #change plan & start_subs_time
    self.plan = new_plan
    self.start_subs_time = datetime.now()
    self.invoice = self.plan.price * discount