from django.core.management.base import BaseCommand, CommandError
from go.models import Noun

class Command(BaseCommand):
    args = 'filename'
    help = 'Imports new nouns from a file list'

    def handle(self, *args, **options):
        if not args:
            raise CommandError("File not specified")
        try:
            with open(args[0]) as nouns:
                for noun in nouns:
                    Noun.objects.create(noun=noun.strip())
        except IOError as e:
            raise CommandError(str(e))

