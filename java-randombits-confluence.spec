# TODO:
# - Build it from sources (sorry, -ENOTIME now and it must work today...)
#   Is it main repo? Or just atlassian mirror?
#   http://svn.atlassian.com/svn/public/contrib/confluence/libraries/org.randombits.confluence/confluence-support/tags/4.3.2/
# - split org.randombits.util classes to separata (sub?)package

### # Conditional build:
### %bcond_without	javadoc		# don't build javadoc
### %bcond_without	tests		# don't build and run tests
###
### %if "%{pld_release}" == "ti"
### %bcond_without	java_sun	# build with gcj
### %else
### %bcond_with	java_sun	# build with java-sun
### %endif
### #

%include	/usr/lib/rpm/macros.java

%define		srcname		randombits-confluence
Summary:	org.randombits.confluence java package
Name:		java-randombits-confluence
Version:	4.3.2
Release:	0.1
License:	BSD-Like
Group:		Libraries/Java
Source0:	https://maven.atlassian.com/contrib/org/randombits/confluence/confluence-support/4.3.2/confluence-support-4.3.2.jar
# Source0-md5:	85ff45c4d76eb1cf0996b980e58c5b61
URL:		http://randombits.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
Requires:	jpackage-utils
Provides:	java(org.randombits.confluence)
Provides:	java(org.randombits.util)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes from org.randombits.confluence java package.
Also contains org.randombits.util classes.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}.jar
%{_javadir}/%{srcname}-%{version}.jar
