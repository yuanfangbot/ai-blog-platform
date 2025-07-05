import os
import subprocess
from github import Github

# Platforms to deploy to - each article goes to one platform
PLATFORMS = [
    "GitHubPages", "NetlifyHugoJekyll", "VercelNext.js", "CloudflarePagesCDNSSL", 
    "Render", "FirebaseHostingCLI", "Surge.sh", "Railway", "GitLabPages",
    "DigitalOceanAppPlatform", "CodebergPages", "Neocities", "FleekWeb3IPFS",
    "AmplifyHostingAWS", "Koyeb", "CloudflareR2"
]

# Deployment functions
def deploy_to_platform(platform, filepath):
    # In a real implementation, this would contain the specific deployment commands
    print(f"Deploying {filepath} to {platform}")
    # Example: subprocess.run(f"vercel deploy {filepath} --prod", shell=True)

# Main deployment workflow
if __name__ == "__main__":
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo("yuanfangbot/ai-blog-platform")
    
    # Get newly created articles
    post_files = [f for f in os.listdir("content/posts") if f.endswith(".md")]
    
    # Deploy each article to a unique platform
    for idx, post in enumerate(post_files[:16]):
        deploy_to_platform(PLATFORMS[idx], os.path.join("content/posts", post))