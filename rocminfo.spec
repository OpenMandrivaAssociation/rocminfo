Name:		rocminfo
Version:	6.3.0
Release:	1
Summary:	ROCm system info utility
Group:		System/Configuration/ROCm
License:	NCSA
URL:		https://github.com/RadeonOpenCompute/rocminfo
Source0:	https://github.com/RadeonOpenCompute/rocminfo/archive/rocm-%{version}.tar.gz#/rocminfo-rocm-%{version}.tar.gz
#Patch0:		0001-adjust-CMAKE_CXX_FLAGS.patch
Patch1:		0002-fix-buildtype-detection.patch

BuildSystem:	cmake
BuildOption:	-DROCM_DIR=%{_prefix}
BuildRequires:	cmake(hsa-runtime64)
BuildRequires:	pkgconfig(python)

# rocminfo calls lsmod to check the kernel mode driver status
Requires:		kmod

%description
ROCm system info utility

%prep
%autosetup -n %{name}-rocm-%{version} -p1
python /usr/bin/pathfix.py -i %{__python3} rocm_agent_enumerator

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo
#Duplicated files:
%exclude %{_docdir}/*/License.txt
