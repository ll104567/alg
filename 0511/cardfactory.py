from cardx import Card,AceCard,FaceCard,NumberCard,Suit

class CardFactory:
	
	def rank(self, rank):
		self.class_, self.rank_str = {
		1:(AceCard,'A'),
		11:(FaceCard,'J'),
		12:(FaceCard,'Q'),
		13:(FaceCard,'K'),
		}.get(rank,(NumberCard,str(rank)))
		return self

	def suit(self, suit):
		return self.class_(self.rank_str,suit)

Club,Diamond,Heart,Spade = Suit('Club','C'),Suit('Diamond','D'),Suit('Heart','H'),Suit('Spade','S')

card8 = CardFactory()
deck8 = [card8.rank(r+1).suit(s) for r in range(13) for s in (Club,Diamond,Heart,Spade)]
