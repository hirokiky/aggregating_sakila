% if ranking_table:
<table>
  <thead>
    <tr>
      <th>順位</th>
      <th>タイトル</th>
      <th>合計金額</th>
      <th>合計件数</th>
    </tr>
  </thead>
  <tbody>
    % for i, row in enumerate(ranking_table):
    <tr>
      <td>${i+1}</td>
      % for cell in row:
      <td>${cell}</td>
      % endfor
    </tr>
    % endfor
  </tbody>
</table>
% endif