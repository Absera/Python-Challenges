class Code:

	def run(self):
		code = str(self.main())
		exec(str(self.main()))

