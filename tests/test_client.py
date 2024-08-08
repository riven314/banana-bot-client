import pytest

from func.client import BananaAPIClient


@pytest.fixture
def api_client(monkeypatch):
    def mock_get_tokens():
        return [{"token": "valid_token"}]

    monkeypatch.setattr(
        "func.banana_api_client.BananaAPIClient._get_tokens", mock_get_tokens
    )
    return BananaAPIClient()


def test_claim_lottery(api_client, monkeypatch):
    def mock_validate_tokens():
        return [{"token": "valid_token"}]

    def mock_get(url, headers):
        class MockResponse:
            @staticmethod
            def json():
                return {"data": {"remain_lottery_count": 2, "countdown_end": True}}

            def raise_for_status(self):
                pass

        return MockResponse()

    def mock_post(url, json=None, headers=None):
        class MockResponse:
            def raise_for_status(self):
                pass

        return MockResponse()

    monkeypatch.setattr(
        "func.banana_api_client.BananaAPIClient._validate_tokens", mock_validate_tokens
    )
    monkeypatch.setattr("requests.get", mock_get)
    monkeypatch.setattr("requests.post", mock_post)

    api_client.claim_lottery()
    # Assert statements can be added based on console outputs or further logic


def test_claim_mission(api_client, monkeypatch):
    def mock_validate_tokens():
        return [{"token": "valid_token"}]

    def mock_get(url, headers):
        class MockResponse:
            @staticmethod
            def json():
                return {
                    "data": {
                        "quest_list": [
                            {
                                "quest_id": 1,
                                "is_claimed": False,
                                "is_achieved": False,
                                "quest_name": "mission1",
                            },
                            {
                                "quest_id": 2,
                                "is_claimed": False,
                                "is_achieved": True,
                                "quest_name": "mission2",
                            },
                        ]
                    }
                }
