import credentials
import requests


class GetData:
    @staticmethod
    def get_data_url(url):
        response = requests.get(url, auth=(credentials.username, credentials.password))
        data = response.json()
        return data

    @staticmethod
    def get_data(file):
        # TODO: search file
        response = requests.get(url, auth=(credentials.username, credentials.password))
        data = response.json()
        return data


url = 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text=I' \
          '%20still%20have%20a%20dream%2C%20a%20dream%20deeply%20rooted%20in%20the%20American%20dream%20%E2%80%93' \
          '%20one%20day%20this%20nation%20will%20rise%20up%20and%20live%20up%20to%20its%20creed%2C%20%22We%20hold' \
          '%20these%20truths%20to%20be%20self%20evident%3A%20that%20all%20men%20are%20created%20equal.&features' \
          '=sentiment,keywords'

data = GetData.get_data_url(url)
print(data)
print(data['sentiment']['document']['score'])
print(data['keywords'])
print(data['keywords'][0]['text'])

# data = GetData.get_data('sample.txt')
# print(data)