import os
while(True):
    os.system("clear")
    print("\t\t\t\tWelcome to the Menu for LVM !!")
    print("\t\t\t\t------------------------------")
    print()
    print("\t\t\t1.Create LV(logical volume),PV(physical volume),VG(volume group)")
    print("\t\t\t2.Increase the size of LV(logical volume)")
    print("\t\t\t3.Reduce the size of LV(logical volume)")
    print("\t\t\t4.Mount volume")
    print("\t\t\t5.Display all mounted disk")
    print("\t\t\t6.List all VG(Volume Group)")
    print("\t\t\t7.List all LV(Logical Volume)")
    print("\t\t\t8.List all PV(Physical Volume)")
    print("\t\t\t9.List all harddisks connected to system")
    print("\t\t\t10.exit")
    a=int(input("ENTER YOUR OPTION : "))
    if(a==1):
        no=int(input("enter the number of disks you want to join: "))
        no1=no
        l=[]
        while(no>0):
            c=input("Enter the device name : ")
            l.append(c)
            no-=1
        for i in range (0,no1):
            os.system("pvcreate {}".format(l[i]))
        vgname=input("Enter the volume group name you want to give : ")
        disks=""
        for i in l:
            disks+=i+" "
        os.system("vgcreate {} {}".format(vgname,disks))
        os.system("vgdisplay {}".format(vgname))
        lvmsize=int(input("Enter the logical volume size you want to create in GB : "))
        lvmname=input("Enter the name of logical volume you want to give : ")
        os.system("lvcreate --size {}G --name {} {}".format(lvmsize,lvmname,vgname))
    elif(a==2):
        vgname=input("Enter the name of Volume Group: ")
        lvname=input("Enter the name of logical volume: ")
        os.system("vgdisplay {}".format(vgname))
        size=int(input("Enter the storage you want to increase in GB : "))
        os.system("lvextend --size +{}G /dev/{}/{}".format(size,vgname,lvname))
        os.system("resize2fs /dev/{}/{}".format(vgname,lvname))
    elif(a==3):
        vgname=input("Enter the name of volume group: ")
        lvname=input("Enter the name of logical volume group: ")
        mdir=input("Enter the mounted drive location: ")
        size=int(input("Enter the size you want to reduce in GB : "))
        os.system("umount -f /dev/{}/{}".format(vgname,lvname))
        os.system("e2fsck -f /dev/{}/{}".format(vgname,lvname))
        os.system("resize2fs /dev/{}/{} {}G".format(vgname,lvname,size))
        os.system("lvreduce -L {}G /dev/{}/{}".format(size,vgname,lvname))
        os.system("mount /dev/{}/{} /{}".format(vgname,lvname,mdir))
    elif(a==4):
        dirname=input("Enter the name of mounting directory: ")
        os.system("mkdir /{}".format(dirname))
        vgname=input("Enter the vgname: ")
        lvmname=input("Enter the LVname: ")
        os.system("mount /dev/{}/{} /{}".format(vgname,lvmname,dirname))
    elif(a==5):
        os.system("df -h")
    elif(a==6):
        os.system("vgdisplay")
    elif(a==7):
        os.system("lvdisplay")
    elif(a==8):
        os.system("pvdisplay")
    elif(a==9):
        os.system("fdisk -l")
    elif(a==10):
        exit()
    else:
        print("option not supported")
    input("press any key to continue...")