"""
Python classes representing the Lord's Prayer RDF Schema.

This module provides object-oriented representations of the RDFS classes
defined in lords_prayer.ttl.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Petition:
    """A request or plea within a prayer."""

    text: str
    order: int
    concerns: str
    label: Optional[str] = None

    def __post_init__(self):
        if self.label is None:
            self.label = f"Petition {self.order - 1}"


@dataclass
class Doxology:
    """An expression of praise to God."""

    text: str
    order: int
    label: str = "Doxology"


@dataclass
class Prayer:
    """A formal religious address to God or a deity."""

    invocation: str
    petitions: List[Petition] = field(default_factory=list)
    doxology: Optional[Doxology] = None
    addressed_to: Optional[str] = None
    label: Optional[str] = None

    def add_petition(self, text: str, order: int, concerns: str, label: Optional[str] = None) -> Petition:
        """Add a petition to the prayer."""
        petition = Petition(text=text, order=order, concerns=concerns, label=label)
        self.petitions.append(petition)
        return petition

    def set_doxology(self, text: str, order: int) -> Doxology:
        """Set the doxology for the prayer."""
        self.doxology = Doxology(text=text, order=order)
        return self.doxology

    def get_petitions_in_order(self) -> List[Petition]:
        """Return petitions sorted by order."""
        return sorted(self.petitions, key=lambda p: p.order)

    def __str__(self) -> str:
        """Return a formatted string representation of the prayer."""
        lines = []
        if self.label:
            lines.append(f"=== {self.label} ===\n")

        lines.append(self.invocation)

        for petition in self.get_petitions_in_order():
            lines.append(petition.text)

        if self.doxology:
            lines.append(self.doxology.text)

        return "\n".join(lines)


# Example: Instantiate the Lord's Prayer
def create_lords_prayer() -> Prayer:
    """Create an instance of the Lord's Prayer using the Python classes."""

    prayer = Prayer(
        invocation="Our Father who art in heaven",
        addressed_to="God the Father",
        label="The Lord's Prayer"
    )

    # Add petitions
    prayer.add_petition(
        text="Hallowed be thy name",
        order=2,
        concerns="Sanctification of God's name",
        label="First Petition"
    )

    prayer.add_petition(
        text="Thy kingdom come",
        order=3,
        concerns="Coming of God's kingdom",
        label="Second Petition"
    )

    prayer.add_petition(
        text="Thy will be done on earth as it is in heaven",
        order=4,
        concerns="Fulfillment of God's will",
        label="Third Petition"
    )

    prayer.add_petition(
        text="Give us this day our daily bread",
        order=5,
        concerns="Daily sustenance",
        label="Fourth Petition"
    )

    prayer.add_petition(
        text="And forgive us our trespasses, as we forgive those who trespass against us",
        order=6,
        concerns="Forgiveness",
        label="Fifth Petition"
    )

    prayer.add_petition(
        text="And lead us not into temptation",
        order=7,
        concerns="Protection from temptation",
        label="Sixth Petition"
    )

    prayer.add_petition(
        text="But deliver us from evil",
        order=8,
        concerns="Deliverance from evil",
        label="Seventh Petition"
    )

    # Add doxology
    prayer.set_doxology(
        text="For thine is the kingdom, and the power, and the glory, forever. Amen.",
        order=9
    )

    return prayer


if __name__ == "__main__":
    # Demonstrate usage
    lords_prayer = create_lords_prayer()
    print(lords_prayer)

    print("\n" + "="*50)
    print("Prayer Details:")
    print(f"Addressed to: {lords_prayer.addressed_to}")
    print(f"Number of petitions: {len(lords_prayer.petitions)}")

    print("\nPetitions by concern:")
    for petition in lords_prayer.get_petitions_in_order():
        print(f"  - {petition.concerns}: \"{petition.text}\"")
