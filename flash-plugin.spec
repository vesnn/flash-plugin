%define debug_package %{nil}

Summary:    Adobe Flash Player 27
Name:       flash-plugin
Version:    28.0.0.126
Release:    1%{?dist}
Epoch:      7

Group:      Applications/Internet
License:    Proprietary
URL:        http://www.adobe.com
Source0:    https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_npapi_linux.i386.tar.gz
Source1:    https://fpdownload.adobe.com/pub/flashplayer/pdc/%{version}/flash_player_npapi_linux.x86_64.tar.gz

Provides:   flash-plugin-meta
AutoReq:    on


%description
Adobe Flash (formerly Macromedia Flash) is a multimedia platform used to
add animation, video, and interactivity to Web pages. Flash is frequently
used for advertisements and games. More recently, it has been positioned
as a tool for "Rich Internet Applications" ("RIAs").

%package kde
Summary:    KDE workspace files
Group:      Applications/Internet
Requires:   %{name} = %{epoch}:%{version}


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
%else
tar xzf %{SOURCE0}
%endif
mv libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}/readme.txt %{buildroot}%{_pkgdocdir}/
mv %{buildroot}/license.pdf %{buildroot}%{_pkgdocdir}/
mv %{buildroot}/LGPL/LGPL.txt %{buildroot}%{_pkgdocdir}/
mv %{buildroot}/LGPL/notice.txt %{buildroot}%{_pkgdocdir}/
rmdir %{buildroot}/LGPL/

%ifarch x86_64
rm -rf %{buildroot}/usr/lib/kde4/
%endif


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
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/flash-player-properties.png
%{_datadir}/pixmaps/flash-player-properties.png
%docdir %{_pkgdocdir}
%doc %{_pkgdocdir}/readme.txt
%doc %{_pkgdocdir}/license.pdf
%doc %{_pkgdocdir}/LGPL.txt
%doc %{_pkgdocdir}/notice.txt

%files kde
%defattr(-, root, root, -)
%{_libdir}/kde4/kcm_adobe_flash_player.so
%{_datadir}/kde4/services/kcm_adobe_flash_player.desktop


%changelog
* Thu Dec 14 2017 VSE NN <metanoite@rambler.ru> - 7:28.0.0.126-1
- update to 28.0.0.126

* Thu Nov 16 2017 VSE NN <metanoite@rambler.ru> - 7:27.0.0.187-1
- update to 27.0.0.187

* Mon Nov 06 2017 VSE NN <metanoite@rambler.ru> - 7:27.0.0.183-1
- update to 27.0.0.183

* Sat Oct 21 2017 VSE NN <metanoite@rambler.ru> - 7:27.0.0.170-1
- update to 27.0.0.170

* Thu Oct 12 2017 VSE NN <metanoite@rambler.ru> - 7:27.0.0.159-1
- update to 27.0.0.159

* Tue Sep 12 2017 VSE NN <metanoite@rambler.ru> - 7:27.0.0.130-1
- update to 27.0.0.130

* Wed Aug 09 2017 VSE NN <metanoite@rambler.ru> - 7:26.0.0.151-1
- update to 26.0.0.151

* Fri Jul 14 2017 VSE NN <metanoite@rambler.ru> - 7:26.0.0.137-1
- update to 26.0.0.137

* Wed Jun 21 2017 VSE NN <metanoite@rambler.ru> - 7:26.0.0.131-1
- update to 26.0.0.131

* Wed Jun 14 2017 VSE NN <metanoite@rambler.ru> - 7:26.0.0.126-1
- update to 26.0.0.126

* Fri May 26 2017 VSE NN <metanoite@rambler.ru> 7:25.0.0.171-2
- replace erroneous source archives from the previous 25.0.0.148
  version by the actual 25.0.0.171 ones

* Mon May 15 2017 VSE NN <metanoite@rambler.ru> 7:25.0.0.171-1
- update to 25.0.0.171

* Wed Apr 12 2017 VSE NN <metanoite@rambler.ru> 7:25.0.0.148-1
- update to 25.0.0.148

* Thu Mar 16 2017 VSE NN <metanoite@rambler.ru> 7:25.0.0.127-1
- update to 25.0.0.127

* Wed Feb 15 2017 VSE NN <metanoite@rambler.ru> 7:24.0.0.221-1
- update to 24.0.0.221

* Sun Jan 15 2017 VSE NN <metanoite@rambler.ru> 7:24.0.0.194-1
- update to 24.0.0.194

* Thu Dec 22 2016 VSE NN <metanoite@rambler.ru> 7:24.0.0.186-1
- update to 24.0.0.186

* Fri Nov 11 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.644-1
- update to 11.2.202.644

* Wed Nov 02 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.643-1
- update to 11.2.202.643

* Thu Oct 20 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.637-1
- update to 11.2.202.637

* Sat Sep 17 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.635-1
- update to 11.2.202.635

* Wed Jul 20 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.632-1
- update to 11.2.202.632

* Sat Jun 18 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.626-1
- update to 11.2.202.626

* Sun May 15 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.621-1
- update to 11.2.202.621

* Mon Apr 11 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.616-1
- update to 11.2.202.616

* Fri Mar 11 2016 Arkady L. Shane <ashejn@russianfedora.pro> 7:11.2.202.577-1.R
- update to 11.2.202.577

* Wed Feb 10 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.569-1
- update to 11.2.202.569

* Tue Jan 26 2016 VSE NN <metanoite@rambler.ru> 7:11.2.202.559-1
- update to 11.2.202.559

* Sun Dec 13 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.554-1
- update to 11.2.202.554

* Wed Nov 11 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.548-1
- update to 11.2.202.548

* Sat Oct 17 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.540-1
- update to 11.2.202.540

* Thu Oct 15 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.535-1
- update to 11.2.202.535

* Fri Sep 25 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.521-1
- update to 11.2.202.521

* Wed Aug 12 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.508-1
- update to 11.2.202.508

* Mon Aug 03 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.491-1
- update to 11.2.202.491

* Fri Jul 10 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.481-1
- update to 11.2.202.481

* Tue Jun 23 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.468-1
- update to 11.2.202.468

* Sat Jun 13 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.466-1
- update to 11.2.202.466

* Thu May 14 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.460-1
- update to 11.2.202.460

* Wed Apr 15 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.457-1
- update to 11.2.202.457

* Sun Mar 15 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.451-1
- update to 11.2.202.451

* Thu Feb 05 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.442-1
- update to 11.2.202.442

* Tue Jan 27 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.440-1
- update to 11.2.202.440

* Thu Jan 22 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.438-1
- update to 11.2.202.438

* Sat Jan 17 2015 VSE NN <metanoite@rambler.ru> 7:11.2.202.429-1
- update to 11.2.202.429

* Thu Dec 11 2014 VSE NN <metanoite@rambler.ru> 7:11.2.202.425-1
- update to 11.2.202.425

* Fri Nov 28 2014 VSE NN <metanoite@rambler.ru> 7:11.2.202.424-1
- update to 11.2.202.424

* Wed Nov 12 2014 VSE NN <metanoite@rambler.ru> 7:11.2.202.418-1
- update to 11.2.202.418

* Sat Oct 18 2014 VSE NN <metanoite@rambler.ru> 7:11.2.202.411-1
- update to 11.2.202.411

* Thu Sep 11 2014 VSE NN <metanoite@rambler.ru> 7:11.2.202.406-1
- update to 11.2.202.406

* Tue Aug  2 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.400-1.R
- update to 11.2.202.400

* Wed Apr 30 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.356-1.R
- update to 11.2.202.356

* Mon Mar 17 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.346-3.R
- and in kde package too

* Mon Mar 17 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.346-2.R
- pack only files

* Mon Mar 17 2014 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.346-1.R
- update to 11.2.202.310

* Mon Sep 30 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.310-1.R
- update to 11.2.202.310

* Mon Jul 22 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.297-1.R
- update to 11.2.202.297

* Wed Apr 12 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.280-1.R
- update to 11.2.202.280

* Thu Feb 28 2013 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.273-1.R
- update to 11.2.202.273

* Mon Oct 15 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.243-1.R
- update to 11.2.202.243

* Fri Aug 24 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.238-1.R
- update to 11.2.202.238

* Thu Jun 14 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.236-1.R
- update to 11.2.202.236

* Mon May 14 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.2.202.235-1.R
- update to 11.2.202.235

* Thu Apr 26 2012 Arkady L. Shane <ashejn@russianfedora.ru> 7:11.1.102.63-2.R
- back to old flash.

* Mon Apr  2 2012 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.2.202.228-1.R
- update to 11.2.202.228. Last?

* Wed Mar  7 2012 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.1.102.63-1.R
- update to 11.1.102.63

* Fri Feb 17 2012 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.1.102.62-1.R
- update to 11.1.102.62

* Mon Nov 14 2011 Arkady L. Shane <ashejn@russianfedora.ru> 6:11.1.102.55-1.R
- update to 11.1.102.55

* Tue Oct 04 2011 Vasiliy N. Glazov <vascom2@gmail.com> 6:11.0.1.152-1.R
- update to 11.0.1.152

* Fri Sep 09 2011 Vasiliy N. Glazov <vascom2@gmail.com> 6:11.0.r1.129-1.R
- update to 11.0.r1.129

* Thu Jul 14 2011 Arkady L. Shane <ashejn@yandex-team.ru> 6:11.0.1.60-3.R
- fix R in kde

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
