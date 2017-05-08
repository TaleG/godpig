# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-02 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('godbody', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(choices=[('server', '物理机'), ('openstack', '云虚拟机'), ('switch', '交换机'), ('router', '路由器'), ('firewall', '防火墙'), ('storage', '存储设备'), ('NLB', '负载均衡'), ('wireless', '无线AP'), ('software', '软件资产'), ('others', '其它类')], default='server', max_length=64, verbose_name='设备类型')),
                ('name', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='设备名')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='资产SN号')),
                ('production_test', models.IntegerField(choices=[(1, '生产'), (2, '测试')], default=1, verbose_name='生产／测试')),
                ('model', models.CharField(blank=True, max_length=12, null=True, verbose_name='机柜号')),
                ('model_position', models.CharField(blank=True, max_length=12, null=True, verbose_name='机柜位置')),
                ('management_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('ip1', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth1')),
                ('ip2', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth2')),
                ('ip3', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth3')),
                ('ip4', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth4')),
                ('raid_type', models.CharField(blank=True, max_length=512, null=True, verbose_name='raid类型')),
                ('trade_data', models.DateField(blank=True, null=True, verbose_name='购买时间')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='过保修期')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='价格')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godbody.UserProfile', verbose_name='管理员')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='业务线')),
                ('name_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='业务子线路')),
                ('memo', models.CharField(blank=True, max_length=64, verbose_name='备注')),
                ('parent_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_level', to='godcmdb.BusinessUnit')),
            ],
            options={
                'verbose_name': '业务线',
                'verbose_name_plural': '业务线',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='合同号')),
                ('name', models.CharField(max_length=64, verbose_name='合同名称')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('price', models.IntegerField(verbose_name='合同金额')),
                ('datail', models.TextField(blank=True, null=True, verbose_name='合同详细')),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('license_num', models.IntegerField(blank=True, verbose_name='License数量')),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': '合同',
                'verbose_name_plural': '合同',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True, verbose_name='CPU型号')),
                ('cpu_count', models.SmallIntegerField(blank=True, null=True, verbose_name='物理CPU个数')),
                ('cpu_core_count', models.SmallIntegerField(blank=True, null=True, verbose_name='CPU核数')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('creat_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'CPU部件',
                'verbose_name_plural': 'CPU部件',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN号')),
                ('slot', models.CharField(blank=True, max_length=64, null=True, verbose_name='插槽位')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='磁盘型号')),
                ('capacity', models.FloatField(verbose_name='磁盘容量GB')),
                ('iface_type', models.CharField(blank=True, choices=[('SATA', 'SATA'), ('SAS', 'SAS'), ('SCSI', 'SCSI'), ('SSD', 'SSD')], default='SAS', max_length=64, null=True, verbose_name='接口类型')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '硬盘',
                'verbose_name_plural': '硬盘',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='机房名称')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '机房',
                'verbose_name_plural': '机房',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufactory', models.CharField(max_length=64, unique=True, verbose_name='厂商名称')),
                ('model', models.CharField(blank=True, max_length=63, null=True, verbose_name='设备型号')),
                ('support_num', models.CharField(blank=True, max_length=30, verbose_name='支持电话')),
                ('memo', models.CharField(blank=True, max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name': '厂商',
                'verbose_name_plural': '厂商',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlan_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='SN号')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('device_detail', models.TextField(blank=True, null=True, verbose_name='设置详细配置')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '网络设备',
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NewAssetApprovalZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='资产SN号')),
                ('asset_type', models.CharField(choices=[('server', '服务器'), ('switch', '交换机'), ('router', '路由器'), ('firewall', '防火墙'), ('storage', '存储设备'), ('NLB', '负载均衡'), ('wireless', '无线AP'), ('software', '软件资产'), ('others', '其它类')], default='服务器', max_length=64)),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True)),
                ('model', models.CharField(blank=True, max_length=128, null=True)),
                ('ram_size', models.IntegerField(blank=True, null=True)),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True)),
                ('cpu_count', models.IntegerField(blank=True, null=True)),
                ('cpu_core_count', models.IntegerField(blank=True, null=True)),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True)),
                ('os_type', models.CharField(blank=True, max_length=64, null=True)),
                ('os_release', models.CharField(blank=True, max_length=64, null=True)),
                ('data', models.TextField(verbose_name='资产数据')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='汇报日期')),
                ('approved', models.BooleanField(default=False, verbose_name='已批准')),
                ('approved_by', models.CharField(blank=True, max_length=64, null=True, verbose_name='申批人')),
                ('approved_date', models.DateTimeField(blank=True, null=True, verbose_name='批准日期')),
            ],
            options={
                'verbose_name': '新上线待批准资产',
                'verbose_name_plural': '新上线待批准次产',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='网卡名')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN号')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='网卡型号')),
                ('macaddress', models.CharField(blank=True, max_length=64, null=True, verbose_name='MAC')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('netmask', models.CharField(blank=True, max_length=64, null=True, verbose_name='子网掩码')),
                ('gateway', models.CharField(blank=True, max_length=64, null=True, verbose_name='网关')),
                ('bonding', models.CharField(blank=True, max_length=64, null=True, verbose_name='bond')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '网卡',
                'verbose_name_plural': '网卡',
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN号')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='内存型号')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='制造商')),
                ('slot', models.CharField(blank=True, max_length=64, null=True, verbose_name='插槽')),
                ('capacity', models.CharField(max_length=64, verbose_name='内存大小(GB)')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'RAM',
                'verbose_name_plural': 'RAM',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(choices=[('auto', '自动'), ('manual', '手动')], default='manual', max_length=32, verbose_name='添加模式')),
                ('ips1', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth1')),
                ('ips2', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth2')),
                ('ips3', models.GenericIPAddressField(blank=True, null=True, verbose_name='eth3')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('IPS', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.NIC', verbose_name='网卡信息')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godbody.UserProfile', verbose_name='项目管理员')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Asset')),
                ('business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.BusinessUnit', verbose_name='所属项目')),
                ('cpu_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.CPU', verbose_name='CPU信息')),
                ('disk_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Disk', verbose_name='磁盘信息')),
                ('hosted_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosted_on_server', to='godcmdb.Server')),
                ('mem_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.RAM', verbose_name='内存信息')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows'), ('network_firmware', 'Network Firmware'), ('software', 'Software')], default='Linux', max_length=128, verbose_name='系统类型')),
                ('distribution', models.CharField(choices=[('windows', 'Windows'), ('centos', 'CentOS'), ('redhat', 'Redhat'), ('esxi', 'ESXI')], default='redhat', max_length=128, verbose_name='类型')),
                ('version', models.CharField(max_length=64, verbose_name='软件／系统版本')),
                ('language', models.CharField(choices=[('cn', '中文'), ('en', '英文')], max_length=128, verbose_name='系统语言')),
            ],
            options={
                'verbose_name': '软件／系统',
                'verbose_name_plural': '软件／系统',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='网卡名')),
            ],
        ),
        migrations.AddField(
            model_name='server',
            name='os_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Software', verbose_name='系统类型'),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='firmware',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Software'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.BusinessUnit', verbose_name='所属项目'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Contract', verbose_name='合同'),
        ),
        migrations.AddField(
            model_name='asset',
            name='cpu_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.CPU', verbose_name='CPU信息'),
        ),
        migrations.AddField(
            model_name='asset',
            name='disk_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Disk', verbose_name='磁盘信息'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.IDC', verbose_name='IDC机房'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufactory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Manufactory', verbose_name='制造商'),
        ),
        migrations.AddField(
            model_name='asset',
            name='mem_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='godcmdb.RAM', verbose_name='内存信息'),
        ),
        migrations.AddField(
            model_name='asset',
            name='os_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='godcmdb.Software', verbose_name='系统类型'),
        ),
    ]
