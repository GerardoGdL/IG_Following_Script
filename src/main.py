from parser.follower_parser import parse_followers
from parser.follower_parser import parse_following
from output.formatter import not_following_me_back

# The main function simply calls the functions required to
# parse the followers and following JSON files, and then
# calls the function to find the people who are not following
# you back. It then prints the results to the console.

def main():
    followers = parse_followers("data/raw/connections/followers_and_following/followers_1.json")
    following = parse_following("data/raw/connections/followers_and_following/following.json")

    results = not_following_me_back(followers, following)

    print("The following people are not following you back:")
    for username in results:
        print(username)

if __name__ == "__main__":
    main()