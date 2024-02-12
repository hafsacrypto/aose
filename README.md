
1) Configure your git username and email

	git config — global user.name “Your Name” git config — global user.email youremail@example.com

2) Generate a new SSH key

	ssh-keygen -t ed25519 -C “youremail@example.com”

3) Let's tell the SSH agent about the new key:

	eval "$(ssh-agent -s)" ssh-add ~/.ssh/id_ed25519

4) Let's copy the key to clipboard:

	pbcopy < ~/.ssh/id_ed25519.pub

5) 
	- Open github.com
	- Go to Settings
	- Go to SSH and GPG keys
	- Click "New SSH Key"
	- Name add whatever, paste the key into the field and just remove the line ending (blank line after the key)