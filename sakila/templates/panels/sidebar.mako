<div class="well sidebar-nav">
    <ul class="nav nav-list">
        % for menu, url in menus:
            % if url:
                % if request.url.startswith(url):
                    <li class="active"><a href="${url}">${menu}</a></li>
                % else:
                    <li><a href="${url}">${menu}</a></li>
                % endif
            % else:
                <li class="nav-header">${menu}</li>
            % endif
        % endfor
    </ul>
</div><!--/.well -->
