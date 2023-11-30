import subprocess

# Function to run shell commands
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

# Run commands to set up Arch Linux (Example steps)
def setup_arch_linux():
    # Example: Partitioning the disk with fdisk
    disk_name = input("disk:\n")
    print("Partitioning the disk with fdisk")
    run_command(f'fdisk {disk_name}')

    # Example: Formatting partitions
    print("Formatting partitions")
    run_command(f'mkfs.ext4 {disk_name}1')  # Format the partition as ext4

    # Example: Mounting partitions
    print("Mounting partitions")
    run_command(f'mount {disk_name}1 /mnt')  # Mount the root partition

    # Example: Install base system
    print("Install base system")
    run_command('pacstrap /mnt base linux linux-firmware')  # Install base packages

    # Example: Generate fstab
    print("Generating fstab")
    run_command('genfstab -U /mnt >> /mnt/etc/fstab')

    # Example: Chroot into the new system
    print("Chroot into the new system")
    run_command('arch-chroot /mnt')

    # Example: Set timezone
    print("Setting timezone")
    run_command('timedatectl')

    # Example: Set hardware clock
    print("Setting hardware clock")
    run_command('hwclock --systohc')

    # Example: Set hostname
    print("Setting hostname")
    run_command('echo "Linux" > /etc/hostname')

    # Example: Set root password
    print("Set root passwd: ")
    run_command('passwd')  # Prompt to set root password

    # Example: Install bootloader (GRUB)
    print("Install bootloader (GRUB)")
    run_command('pacman -S grub')
    run_command(f'grub-install {disk_name}')
    run_command('grub-mkconfig -o /boot/grub/grub.cfg')

    # Example: Enable services (e.g., network)
    print("Enable services (e.g., network)")
    run_command('systemctl enable dhcpcd.service')

    # Example: Exit chroot
    print("Exit chroot")
    run_command('exit')

    # Example: Unmount partitions
    print()
    run_command('umount -R /mnt')

    # Example: Install GNOME and display manager (gdm)
    print("Installing Gnome and display manager (gdm)")
    run_command('pacman -Sy gnome gnome-extra gdm')

    # Example: Enable gdm (GNOME Display Manager)
    print("Enabling gdm (GNOME Display Manager)")
    run_command('systemctl enable gdm')

    print("GNOME Desktop Environment installed.")

    print("Arch Linux installation complete.")

# Call the function to start setup
setup_arch_linux()
