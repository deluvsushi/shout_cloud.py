from requests import post

class ShoutCloud:
	def __init__(self) -> None:
		self.api = "HTTP://API.SHOUTCLOUD.IO/V1"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def capitalize_text(self, text: str) -> dict:
		data = {
			"INPUT": text
		}
		return post(
			f"{self.api}/SHOUT",
			json=data,
			headers=self.headers).json()
