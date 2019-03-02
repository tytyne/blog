from flask_table import Table, Col, LinkCol
class Results(Table):
    Role = Col('role')
    published = Col('Release Date')
    comment= Col('comment')
    blog = Col('blog')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))