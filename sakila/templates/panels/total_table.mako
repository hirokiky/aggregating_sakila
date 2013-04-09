% if total_table:
<table>
  <thead>
    <tr>
      <th>売上金額</th>
      <th>売上件数</th>
    </tr>
  </thead>
  <tbody>
    % for row in total_table:
    <tr>
      % for cell in row:
      <td>${cell}</td>
      % endfor
    </tr>
    % endfor
  </tbody>
</table>
% endif
