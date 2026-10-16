"""Original line icons for the seven advisory disciplines. No external assets."""

DOMAIN_ICONS = {
    # Investment ledger and market-value curve.
    'investments': '<rect x="4" y="3" width="19" height="26" rx="1.5"/><path d="M9 8h9M9 12h5M9 24l5-6 5 3 8-10M23 11h4v4"/>',
    # Insurance protection and a checked accounting policy.
    'technical': '<path d="M16 3 27 7v8c0 7-5 11-11 14C10 26 5 22 5 15V7Z"/><path d="M11 11h10M11 15h7M12 21l3 3 6-7"/>',
    # Consolidated reporting: stacked statements and a financial chart.
    'reporting': '<path d="M7 7H4v22h20v-3"/><rect x="8" y="3" width="20" height="23" rx="1.5"/><path d="M12 8h12M13 21v-5M18 21v-9M23 21v-7M12 21h12"/>',
    # Programme planning: a Gantt chart with three work packages.
    'programme': '<path d="M5 4v24h24M3 8h4M3 16h4M3 24h4"/><rect x="10" y="6" width="12" height="4" rx="1"/><rect x="15" y="14" width="13" height="4" rx="1"/><rect x="10" y="22" width="9" height="4" rx="1"/>',
    # Interim management: a leader and their team.
    'management': '<circle cx="16" cy="8" r="4"/><circle cx="6" cy="12" r="3"/><circle cx="26" cy="12" r="3"/><path d="M9 28v-5a7 7 0 0 1 14 0v5ZM2 26v-5a4 4 0 0 1 6-3.5M30 26v-5a4 4 0 0 0-6-3.5"/>',
    # Industry software: an application window and connected data modules.
    'systems': '<rect x="3" y="4" width="26" height="24" rx="1.5"/><path d="M3 10h26M7 7h1M11 7h1M15 7h1M12 16.5h8M16 16.5V22"/><rect x="7" y="14" width="5" height="5" rx=".5"/><rect x="20" y="14" width="5" height="5" rx=".5"/><rect x="13.5" y="22" width="5" height="4" rx=".5"/>',
    # AI: processor pins and the letters AI, drawn as paths at this small size.
    'ai': '<rect x="7" y="7" width="18" height="18" rx="2"/><path d="M12 3v4M20 3v4M12 25v4M20 25v4M3 12h4M3 20h4M25 12h4M25 20h4M11 20l3-8 3 8M12 17h4M20 12v8"/>',
}


def domain_icon(domain):
    return (f'<svg class="domain-glyph" data-icon="{domain}" viewBox="0 0 32 32" '
            'fill="none" stroke="currentColor" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
            f'{DOMAIN_ICONS[domain]}</svg>')
