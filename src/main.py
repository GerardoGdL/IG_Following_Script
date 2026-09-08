def main():
    followers = parse_followers("data/raw/followers_1.json")
    following = parse_following("data/raw/following.json")

    results = not_following_me_back(followers, following)

    print(results)

if __name__ == "__main__":
    main()