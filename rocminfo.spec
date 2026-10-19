Name:		rocminfo
Version:	10.1.0
Release:	1
Summary:	ROCm system info utility
License:	NCSA
Group:		System/Configuration
URL:		https://github.com/ROCm/rocminfo
Source0:	https://github.com/ROCm/rocm-systems/releases/download/therock-10.1/rocminfo.tar.gz#/rocminfo-%{version}.tar.gz

BuildSystem:	cmake
BuildRequires:	rocm-rpm-macros
BuildRequires:	cmake(hsa-runtime64)
BuildRequires:	pkgconfig(python)
# rocminfo calls lsmod
Requires:	kmod
Requires:	rocm-runtime

%description
ROCm system info utility (rocminfo, rocm_agent_enumerator).

%prep
%autosetup -n rocminfo -p1
# Fix python shebang if needed
if [ -f rocm_agent_enumerator ]; then
	sed -i '1s|#!.*python.*|#!%{_bindir}/python3|' rocm_agent_enumerator 2>/dev/null || true
fi

%files
%doc README.md
%license License.txt
%{_bindir}/rocm_agent_enumerator
%{_bindir}/rocminfo
%exclude %{_docdir}/*/License.txt
