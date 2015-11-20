
# based on Fedora's rdma.spec

Summary: Infiniband/iWARP Kernel Module Initializer
Name: rdma
Version: 1
Release: 1
License: GPL-2.0+
Group: System Environment/Base
Source0: rdma.conf
Source1: 98-rdma.rules
Source2: rdma.service
Source3: rdma-init-kernel
BuildArch: noarch
Requires: udev

%description
User space initialization scripts for the kernel InfiniBand/iWARP drivers

%prep

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/lib/rdma/
install -d %{buildroot}/usr/lib/udev/rules.d/
install -d %{buildroot}/usr/lib/systemd/system/
install -d %{buildroot}/usr/libexec

# Stuff to go into the base package
install -m 0644 %{SOURCE0} %{buildroot}/usr/lib/rdma/rdma.conf
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/udev/rules.d/98-rdma.rules
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/rdma.service
install -m 0755 %{SOURCE3} %{buildroot}/usr/libexec/rdma-init-kernel

%clean
rm -rf %{buildroot}

%post
%systemd_post rdma.service

%preun
%systemd_preun rdma.service

%postun
%systemd_postun

%files
%defattr(-,root,root,-)
/usr/lib/rdma/rdma.conf
/usr/lib/udev/rules.d/98-rdma.rules
/usr/lib/systemd/system/rdma.service
/usr/libexec/rdma-init-kernel
