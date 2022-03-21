class Document(object):
    """
    Class used to represent an Document
    """

    def __init__(self, id_doc: int, number_pages: int, title: str = 'Title', category: str = 'Category', author: str = 'Author'):
        """ Document constructor object.

        """
        self._id_doc = id_doc
        self._number_pages = number_pages
        self._title = title
        self._category = category
        self._author = author
    @property
    def id_doc(self) -> int:
        """
          :rtype: int
        """
        return self._id_doc

    @id_doc.setter
    def id_doc(self, id_doc: int):
        """
        :type: int
        """
        self._id_doc = id_doc

    @property
    def number_pages(self) -> int:
        """
          :rtype: int
        """
        return self._number_pages

    @number_pages.setter
    def number_pages(self, number_pages: int):
        """
        :type: int
        """
        self._number_pages = number_pages

    @property
    def title(self) -> str:
        """
          :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """
        :type: str
        """
        self._title = title

    @property
    def category(self) -> str:
        """
          :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str):
        """
        :type: str
        """
        self._category = category

    @property
    def author(self) -> str:
        """
          :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author: str):
        """
        :type: str
        """
        self._author = author

    def __str__(self):
        """
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_doc, self.number_pages, self. title, self.category, self.author)


if __name__ == '__main__':

    doc = Document(id_doc=123, number_pages=123, title="Hello", category="Its me", author="Edwin")
    doc.author = "Antonio Ruble"
    print(doc)

