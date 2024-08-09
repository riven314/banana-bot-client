sample_get_lottery_info_response = {
    "remain_lottery_count": 1,
    "last_countdown_start_time": 1723175687178,
    "countdown_interval": 480,
    "countdown_end": True,
}

sample_do_lottery_response = {
    "banana_id": 26,
    "name": "Nonana",
    "url": "https://public.carv.io/game/banana/nonana.webp",
    "rarity": 0,
    "ripeness": "Ripe",
    "ripeness_sub_level": 0,
    "daily_peel_limit": 330,
    "sell_exchange_peel": 110,
    "sell_exchange_usdt": 0,
    "exclusive_icon_url": "",
    "count": 1,
}

sample_get_quest_list_response = {
    "quest_list": [
        {
            "quest_id": 30,
            "quest_name": "Join CARV Play to get exclusive banana ",
            "quest_type": "visit_page",
            "show_seq_number": 1000,
            "description": "Join CARV Play to get exclusive banana ",
            "start_link": "https://play.carv.io/",
            "peel": 100,
            "is_achieved": False,
            "is_claimed": False,
            "icon_url": "https://public.carv.io/game/banana/tasks/icon_carv_text.png",
            "args": {
                "banana_reward": {
                    "banana_id": 83,
                    "count": 1,
                    "banana_info": {
                        "banana_id": 83,
                        "name": "CARV x Banana",
                        "url": "https://public.carv.io/game/banana/carv.webp",
                        "rarity": 0,
                        "ripeness": "Fully Ripe",
                        "ripeness_sub_level": 0,
                        "daily_peel_limit": 750,
                        "sell_exchange_peel": 370,
                        "sell_exchange_usdt": 0.01,
                        "exclusive_icon_url": "https://public.carv.io/game/banana/tasks/rewards/icon_special_carv.png",
                        "count": 0,
                    },
                }
            },
        }
    ],
    "progress": "0/3",
    "is_claimed": False,
}

sample_claim_quest_response = {
    "peel": 100,
    "banana_reward": {
        "banana_id": 83,
        "count": 1,
        "banana_info": {
            "banana_id": 83,
            "name": "CARV x Banana",
            "url": "https://public.carv.io/game/banana/carv.webp",
            "rarity": 0,
            "ripeness": "Fully Ripe",
            "ripeness_sub_level": 0,
            "daily_peel_limit": 750,
            "sell_exchange_peel": 370,
            "sell_exchange_usdt": 0.01,
            "exclusive_icon_url": "https://public.carv.io/game/banana/tasks/rewards/icon_special_carv.png",
            "count": 0,
        },
    },
}

sample_click_response = {"peel": 1, "speedup": 0}

sample_get_user_info_response = {
    "user_id": 2104747954,
    "username": "whatdoesmycatsay",
    "peel": 1241,
    "usdt": 0,
    "equip_banana_id": 35,
    "equip_banana": {
        "banana_id": 35,
        "name": "XRaynana",
        "url": "https://public.carv.io/game/banana/xraynana.webp",
        "rarity": 0,
        "ripeness": "Ripe",
        "ripeness_sub_level": 0,
        "daily_peel_limit": 390,
        "sell_exchange_peel": 130,
        "sell_exchange_usdt": 0,
        "exclusive_icon_url": "",
        "count": 1,
    },
    "max_click_count": 390,
    "today_click_count": 390,
    "invite_code": "ITP7NU1",
    "lottery_info": {
        "remain_lottery_count": 1,
        "last_countdown_start_time": 1723175687178,
        "countdown_interval": 480,
        "countdown_end": True,
    },
    "ton_wallet": "",
    "banana_count": 7,
    "speedup_count": 0,
}

sample_get_banana_list_response = {
    "banana_list": [
        {
            "banana_id": 83,
            "name": "CARV x Banana",
            "url": "https://public.carv.io/game/banana/carv.webp",
            "rarity": 0,
            "ripeness": "Fully Ripe",
            "ripeness_sub_level": 0,
            "daily_peel_limit": 750,
            "sell_exchange_peel": 370,
            "sell_exchange_usdt": 0.01,
            "exclusive_icon_url": "https://public.carv.io/game/banana/tasks/rewards/icon_special_carv.png",
            "count": 1,
        },
        {
            "banana_id": 35,
            "name": "XRaynana",
            "url": "https://public.carv.io/game/banana/xraynana.webp",
            "rarity": 0,
            "ripeness": "Ripe",
            "ripeness_sub_level": 0,
            "daily_peel_limit": 390,
            "sell_exchange_peel": 130,
            "sell_exchange_usdt": 0,
            "exclusive_icon_url": "",
            "count": 1,
        },
    ]
}
