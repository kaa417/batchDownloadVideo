import requests
import os

def download_video(video_url, file_name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Referer': 'https://www.douyin.com/',  # 必须加上，绕过防盗链
        'Accept': '*/*',
        'Connection': 'keep-alive',
    }

    try:
        response = requests.get(video_url, headers=headers, timeout=15, stream=True)
        if response.status_code == 200:
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"[成功] 下载完成：{file_name}")
        else:
            print(f"[失败] 状态码: {response.status_code} - {video_url}")
    except Exception as e:
        print(f"[异常] 下载错误: {video_url} - {e}")

def batch_download(video_urls, save_dir='videos'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, url in enumerate(video_urls, start=1):
        file_name = os.path.join(save_dir, f"douyin_{i}.mp4")
        download_video(url, file_name)

# 粘贴你的视频真实地址列表(注意：抖音的通过网页获取的视频地址会在几个小时后发生改变（抖音视频保护），建议每次要下载之前再获取视频地址，避免地址过期)
video_urls = ['https://v3-default.365yg.com/1d876ee5b35ac1d670da10479bcd0075/6811f1c9/video/tos/cn/tos-cn-ve-15c001-alinc2/okrPEuD9TAgdncDIANgFiDVLIfbfomEByQ7xOA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=994&bt=994&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApDfzzUvrKsyUc2do0g3cI&mime_type=video_mp4&qs=0&rc=M2dnNTdkPGY7ZDM8aDVoZEBpMzV2eHI5cnN3MzMzNGkzM0AwMmMyMjRfNTUxYTReLjI0YSNrZV9tMmRrcTNhLS1kLTBzcw%3D%3D&btag=c0000e00028000&dy_q=1746002764&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2025043016460410B4E5EDBBB47D736708',
              'https://v26-default.365yg.com/e7d785d925426ce59c82e2c23695cc84/6811f20f/video/tos/cn/tos-cn-ve-15/ogQi1GTxIo6ACDBB3NtBfA0eTDAiQulgNmX0Ed/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1024&bt=1024&cs=0&ds=4&ft=k7Fz7VVywSyRKJ8kmo~pK7pswApGtzzUvrKLO~ycdo0g3cI&mime_type=video_mp4&qs=0&rc=Mzg4PDszZzM2NTozO2k6ZUBpM3FvOnQ5cjRkMzMzNGkzM0AuYC8zLzZhNjQxXy0tMy8tYSNuNGJoMmRzZzNhLS1kLS9zcw%3D%3D&btag=80000e00028000&dy_q=1746002834&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=202504301647143F617DDEB539E9BFA040'
   
]

batch_download(video_urls)
