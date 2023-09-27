# Installation and Setup Guide for Project Naomi on Raspberry Pi

**Note:** Before you begin, make sure you have a Raspberry Pi set up with Raspbian or Raspberry Pi OS installed.

## Installing and Setting Up Project Naomi on Raspberry Pi

1. **Update Your Raspberry Pi:**

   Open a terminal on your Raspberry Pi and run the following commands to ensure your system is up to date:

   ```shell
   sudo apt-get update
   sudo apt-get upgrade
   ```

2. **Install Required Dependencies:**

   Naomi requires several dependencies to work correctly. Install them by running:

   ```shell
   sudo apt-get install python3-pip libopenjp2-7 libtiff5 libatlas-base-dev python3-dev sox portaudio19-dev
   ```

3. **Install Naomi:**

   Install Naomi by running the following command:

   ```shell
   pip3 install naomi
   ```

4. **Set Up Naomi:**

   Run the following command to set up Naomi for the first time:

   ```shell
   naomi-setup
   ```

   Follow the on-screen instructions to configure Naomi. This includes setting your preferred wake word (e.g., "Naomi"), configuring audio input/output, and choosing plugins.

5. **Start Naomi:**

   Once the setup is complete, start Naomi with:

   ```shell
   naomi
   ```

   Naomi should now be running on your Raspberry Pi.

Certainly, here's an updated guide that includes instructions on installing the Recipe Manager Plugin from a GitHub repository:

## Installing the Recipe Manager Plugin

### Method 1: Manual Installation

#### Create a Plugin Directory:

Inside your Naomi installation folder, create a directory for your custom plugins. You can name it `plugins`. Use the following command to create the directory:

```bash
mkdir /path/to/naomi/plugins
```

#### Create the Plugin File:

Inside the `plugins` directory, create a Python file for the Recipe Manager Plugin. You can name it, for example, `recipe_plugin.py`. You can create this file using a text editor or terminal-based editors like nano or vim.

#### Copy and Paste the Plugin Code:

Open the `recipe_plugin.py` file and copy and paste the code for the Recipe Manager Plugin into this file. Make sure to adjust the code as needed, including adding any custom ingredients and recipes.

#### Save the Plugin File:

Save the `recipe_plugin.py` file in the `plugins` directory.

#### Restart Naomi:

Restart Naomi to load the new plugin:

```bash
naomi
```

### Method 2: Installation from GitHub Repository

#### Clone the GitHub Repository:

If the Recipe Manager Plugin is available on a GitHub repository, you can install it by cloning the repository. Navigate to the directory where you want to install the plugin and run:

```bash
git clone https://github.com/your_username/your_repository.git
```

Replace `https://github.com/your_username/your_repository.git` with the actual URL of the GitHub repository.

#### Install the Plugin:

After cloning the repository, navigate to the newly created directory containing the plugin files. You should see the `recipe_plugin.py` file inside. If not, make sure you are in the correct directory.

#### Copy the Plugin File:

Copy the `recipe_plugin.py` file from the cloned repository directory to your Naomi `plugins` directory. You can use the following command to do this:

```bash
cp recipe_plugin.py /path/to/naomi/plugins
```

Replace `/path/to/naomi` with the actual path to your Naomi installation.

#### Restart Naomi:

Restart Naomi to load the new plugin:

```bash
naomi
```

With these instructions, you can either manually create the plugin file or install it from a GitHub repository, depending on your preferred method.

## Using the Recipe Manager Plugin

Now that you have the Recipe Manager Plugin installed:

- To add ingredients, use commands like "Add one apple" or "Add two cups of flour."
- To find recipes, ask Naomi "What can I make?"

The Recipe Manager Plugin will help you manage your ingredients and suggest recipes based on what you have available.
```
