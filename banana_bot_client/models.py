from typing import List, Optional

from pydantic import BaseModel


class LotteryInfoModel(BaseModel):
    remain_lottery_count: int
    last_countdown_start_time: int
    countdown_interval: int
    countdown_end: bool


class DoLotteryModel(BaseModel):
    banana_id: int
    name: str
    url: str
    rarity: int
    ripeness: str
    ripeness_sub_level: int
    daily_peel_limit: int
    sell_exchange_peel: int
    sell_exchange_usdt: float
    exclusive_icon_url: Optional[str]
    count: int


class BananaInfoModel(BaseModel):
    banana_id: int
    name: str
    url: str
    rarity: int
    ripeness: str
    ripeness_sub_level: int
    daily_peel_limit: int
    sell_exchange_peel: int
    sell_exchange_usdt: float
    exclusive_icon_url: Optional[str]
    count: int


class BananaRewardModel(BaseModel):
    banana_id: int
    count: int
    banana_info: Optional[BananaInfoModel]


class QuestModel(BaseModel):
    quest_id: int
    quest_name: str
    quest_type: str
    show_seq_number: int
    description: str
    start_link: Optional[str]
    peel: int
    is_achieved: bool
    is_claimed: bool
    icon_url: str
    args: Optional[
        dict
    ]  # Depending on the structure, this might need more detailed modeling


class QuestListModel(BaseModel):
    quest_list: List[QuestModel]
    progress: str
    is_claimed: bool


class ClaimQuestModel(BaseModel):
    peel: int
    banana_reward: BananaRewardModel


class ClickRewardModel(BaseModel):
    peel: int
    speedup: int


class EquipBananaModel(BaseModel):
    banana_id: int
    name: str
    url: str
    rarity: int
    ripeness: str
    ripeness_sub_level: int
    daily_peel_limit: int
    sell_exchange_peel: int
    sell_exchange_usdt: float
    exclusive_icon_url: Optional[str]
    count: int


class UserInfoModel(BaseModel):
    user_id: int
    username: str
    peel: int
    usdt: int
    equip_banana_id: int
    equip_banana: EquipBananaModel
    max_click_count: int
    today_click_count: int
    invite_code: str
    lottery_info: LotteryInfoModel
    ton_wallet: Optional[str]
    banana_count: int
    speedup_count: int


class BananaModel(BaseModel):
    banana_id: int
    name: str
    url: str
    rarity: int
    ripeness: str
    ripeness_sub_level: int
    daily_peel_limit: int
    sell_exchange_peel: int
    sell_exchange_usdt: float
    exclusive_icon_url: Optional[str]
    count: int


class BananaListModel(BaseModel):
    banana_list: List[BananaModel]
