Summary:	Adobe Flash Player 11
Name:		flash-plugin
Version:	11.0.1.60
Release:	2.R
Epoch:		6

Group:		Applications/Internet
License:	Proprietary
URL:		http://www.adobe.com
Source0:	http://download.macromedia.com/pub/labs/flashplatformruntimes/flashplayer11/flashplayer11_b1_install_lin_32_071311.tar.gz
Source1:	http://download.macromedia.com/pub/labs/flashplatformruntimes/flashplayer11/flashplayer11_b1_install_lin_64_071311.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:	flash-plugin-meta
AutoReq:	on


%description
Adobe Flash (formerly Macromedia Flash) is a multimedia platform used to
add animation, video, and interactivity to Web pages. Flash is frequently
used for advertisements and games. More recently, it has been positioned
as a tool for "Rich Internet Applications" ("RIAs").

%package kde
Summary:	KDE workspace files
Group:          Applications/Internet
Requires:	flash-plugin = %{version}


%description kde
Adobe Flash files to work with KDE


%prep
%setup -q -c -T 


%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

pushd %{buildroot}

mkdir -p %{buildroot}%{_libdir}/mozilla/plugins/
%ifarch x86_64
tar xzf %{SOURCE1}
mv usr/lib/* usr/lib64
rmdir usr/lib
%else
tar xzf %{SOURCE0}
%endif
mv libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null ||:


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database %{_datadir}/applications &> /dev/null ||:


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
%{_bindir}/flash-player-properties
%attr(0755,root,root) %{_libdir}/mozilla/plugins/*.so
%{_libdir}/kde4/kcm_adobe_flash_player.so
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*

%files kde
%defattr(-, root, root, -)
%{_datadir}/kde4/*


%changelog
* Thu Jul 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> 6:11.0.1.60-2.R
- create separate package for KDE

* Thu Jul 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> 6:11.0.1.60-1
- update to 11.0.1.60

* Thu Nov 18 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.161.23-2
- apply https://bugzilla.redhat.com/show_bug.cgi?id=638477#c94 hack

* Wed Sep 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.161.23-1
- update to preview 2 10.2.161.23

* Mon Sep 20 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 10.2.161.22-1
- update to preview 1 10.2.161.22

* Mon Aug  3 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.32.18-1
- update to 10.0.32.18

* Fri Feb 27 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.22.87-1
- update to 10.0.22.87

* Mon Dec 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.15.3-2
- drop x86_64 compatibility

* Fri Dec 19 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.15.3-1
- update to 10.0.15.3

* Mon Nov 17 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-2
- remove depends on libflashsupport

* Wed Oct 15 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 10.0.12.36-1
- update to 10.0.12.36

* Thu May 22 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 9.0.124.0-1
- try to do everything for x86_64