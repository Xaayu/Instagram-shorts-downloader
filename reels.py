import instaloader

L = instaloader.Instaloader()
url = input("Reel link paste karo: ")

# Download the reel
reel_shortcode = url.split("/")[-2]  # Extract reel ID
post = instaloader.Post.from_shortcode(L.context, reel_shortcode)
L.download_post(post, target="reels")