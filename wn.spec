%if %{?rhel}%{!?rhel:0} >= 7
%global el6 0
%else
%global el6 1
%endif

Name:		wn
Version:	4.0.5
Release:	1%{?dist}
Summary:	WN meta-packages
Group:		Applications/Internet
License:	ASL 2.0
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires:       c-ares  
Requires:       cleanup-grid-accounts  
Requires:       cvmfs
Requires:       dcache-srmclient
Requires:       dcap
Requires:       dcap-devel  
Requires:       dcap-libs  
Requires:       dcap-tunnel-gsi  
Requires:       dcap-tunnel-krb  
Requires:       dcap-tunnel-ssl  
Requires:       dcap-tunnel-telnet
Requires:       dpm
Requires:       libdpm.so.1()(64bit),  dpm-libs
Requires:       dpm-devel
Requires:       dpm-perl
Requires:	      dpm-python
Requires:	      fetch-crl
Requires:       gfal2-all
Requires:       gfal2-python
Requires:	      gfal2-util
Requires:       gfalFS
Requires:       gfal2-all
Requires:       gfal2-doc
Requires:       gfal2-devel
Requires:	      ginfo
Requires:       lcg-info  
Requires:       lcg-ManageVOTag
Requires:       lcg-tags
Requires:       lcgdm-devel
Requires:       globus-gass-copy-progs
Requires:       globus-proxy-utils
Requires:	      glite-yaim-core
Requires:       gridsite-libs
Requires:       lcg-infosites  
Requires:       lfc  
Requires:       lfc-devel
Requires:       lfc-perl
Requires:       liblfc.so.1()(64bit), lfc-libs
Requires:       openldap-clients
Requires:       python-ldap  
Requires:       uberftp
Requires:       voms-clients-java
Requires:       voms-devel  
Requires:       xrootd-client  
%if %el6
Requires:	      a1_grid_env  
Requires:       libdpm.so.1
Requires:       emi-version
Requires:       emi.amga.amga-cli
Requires:       emi.saga-adapter.context-cpp
Requires:       emi.saga-adapter.isn-cpp  
Requires:       emi.saga-adapter.sd-cpp  
Requires:       libgfal.so.1()(64bit), libgfal.so.1, gfal
Requires:       gfal-python
Requires:       glite-jobid-api-c  
Requires:       glite-lb-client  
Requires:       glite-lb-common  
Requires:       glite-lb-client-progs
Requires:       glite-lbjp-common-gss  
Requires:       glite-lbjp-common-trio  
Requires:       glite-service-discovery-api-c  
Requires:       glite-wms-brokerinfo-access  
Requires:       glite-wn-info  
Requires:	      glite-yaim-clients
Requires:       jclassads
Requires:       lcgdm-devel(x86-32)
Requires:       liblcgdm.so.1()(64bit), liblcgdm.so.1, lcgdm-libs  
Requires:       lcg-util
Requires:       liblfc.so.1
Requires:	      liblcg_util.so.1()(64bit), liblcg_util.so.1, lcg-util-libs  
Requires:       lcg-util-python
%endif
Source:         wn-4.0.5.tar.gz


%description
List of WN dependencies (APIs & clients).

%prep

%build
# Nothing to do

%install
rm -rf $RPM_BUILD_ROOT
 mkdir -p $RPM_BUILD_ROOT
 find $RPM_BUILD_ROOT -name '*.la' -exec rm -rf {} \;
 find $RPM_BUILD_ROOT -name '*.pc' -exec sed -i -e "s|$RPM_BUILD_ROOT||g" {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%changelog
* Thu Jun 01 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.5-1
- renamed to wn
* Wed May 24 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.4-1
- removed glite-lb-client-progs and deps, added xrootd-client
* Thu Mar 30 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.3-1
- added glite-yaim-core and cvmfs
* Thu Mar 09 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.2-1
- removed umd-release packages as they contain the UMD repos
- added glite-lb-client-progs and deps
* Wed Feb 01 2017 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.1-1
- added dcache-srm-client and umd-release packages to C7
* Mon Sep 05 2016 Andrea Manzi <andrea.manzi@cern.ch> - 4.0.0-1
- first build for C7
- remove SL5 support
* Sun Sep 07 2014 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.1.0-1
- added dependecies on gfal2-util and ginfo (IGIRTC-176)
* Mon Sep 09 2013 Adrien Devresse <adevress at cern.ch> - 3.0.2-2 
- fix for lcgdm-devel 32 bits dependency problem on EL5
* Thu Feb 14 2013 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 3.0.0-1
- added gfal2-doc and gfal2-devel
* Thu Oct 11 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.1-1
- passing to the final versioning
* Fri Oct 05 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-4
- Updated deps according to DM Integration/Clients
* Fri Aug 31 2012 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 2.0.0-3
- Added missing dependencis to the EMI 2 version (includes 32b)
* Fri Apr 01 2011 Cristina Aiftimiei <cristina.aiftimiei@pd.infn.it> - 1.0.0-0
- First version for EMI

