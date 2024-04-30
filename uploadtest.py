import streamlit as st
import subprocess
import os

# Function to switch user
def switch_user(user_id):
    command = f"su -t 'access' -r {user_id}"
    subprocess.run(command, shell=True)

# Function to download files
def download_files(user_id, file_paths):
    switch_user(user_id)
    for file_path in file_paths:
        # Download the file using wget or any other method
        # For simplicity, I'll just copy the file to the current directory
        subprocess.run(f"cp {file_path} .", shell=True)
        st.write(f"File downloaded: {os.path.basename(file_path)}")

# Streamlit UI
def main():
    st.title("File Downloader")

    # List of users
    users = ["user1", "user2", "user3"]
    selected_user = st.selectbox("Select User", users)

    # List of files for each user
    user_files = {
        "user1": ["/nas/path/to/user1/file1", "/nas/path/to/user1/file2"],
        "user2": ["/nas/path/to/user2/file3", "/nas/path/to/user2/file4"],
        "user3": ["/nas/path/to/user3/file5", "/nas/path/to/user3/file6"]
    }

    if st.button("Download Files"):
        if selected_user in user_files:
            download_files(selected_user, user_files[selected_user])
        else:
            st.error("User not found")

if __name__ == "__main__":
    main()
