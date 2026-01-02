from django.core.management.base import BaseCommand
from videos.models import Category, Video
from quizzes.models import Quiz, Question, Answer


class Command(BaseCommand):
    help = 'Populate database with sample video data'

    def handle(self, *args, **options):
        try:
            self.stdout.write("Creating sample data...")

            # Create categories
            categories_data = [
                {
                    'name': 'Plastik ifloslanish',
                    'slug': 'plastik-ifloslanish',
                    'description': 'Plastik chiqindilar va ularning tabiatga ta\'siri',
                    'icon': 'fa-recycle'
                },
                {
                    'name': 'Havo ifloslanishi',
                    'slug': 'havo-ifloslanishi',
                    'description': 'Havo sifati va atmosfera muammolari',
                    'icon': 'fa-wind'
                },
                {
                    'name': 'Suv ifloslanishi',
                    'slug': 'suv-ifloslanishi',
                    'description': 'Suv resurslari va ularning muhofazasi',
                    'icon': 'fa-water'
                },
                {
                    'name': 'O\'rmonlar kesilishi',
                    'slug': 'ormonlar-kesilishi',
                    'description': 'O\'rmonlarning yo\'qolishi va ekologik oqibatlar',
                    'icon': 'fa-tree'
                },
                {
                    'name': 'Yovvoyi tabiat',
                    'slug': 'yovvoyi-tabiat',
                    'description': 'Yovvoyi tabiatni asrash va biodiversitet',
                    'icon': 'fa-leaf'
                },
            ]

            for cat_data in categories_data:
                category, created = Category.objects.get_or_create(
                    slug=cat_data['slug'],
                    defaults=cat_data
                )
                if created:
                    self.stdout.write(f"[+] Created category: {category.name}")

            # Create sample videos
            videos_data = [
                {
                    'title': 'Plastik ifloslanish',
                    'slug': 'plastik-ifloslanish',
                    'description': 'Plastik nega xavfli? U tabiatni qanday ifloslantiradi va biz uni kamaytirish uchun nimalar qilishimiz mumkinligi haqida bilib oling!',
                    'youtube_url': 'https://www.youtube.com/embed/X7fd43sDWLw',
                    'category_slug': 'plastik-ifloslanish',
                    'author_name': 'Nurjahon',
                    'author_role': 'Video developer',
                },
                {
                    'title': 'Havo ifloslanishi',
                    'slug': 'havo-ifloslanishi',
                    'description': 'Havo nega ifloslanadi? Tutun, chang va gazlarning ta\'siri haqida.',
                    'youtube_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                    'category_slug': 'havo-ifloslanishi',
                    'author_name': 'Abdumalik',
                    'author_role': 'Environmental Expert',
                },
                {
                    'title': 'Suv ifloslanishi',
                    'slug': 'suv-ifloslanishi',
                    'description': 'Suv nima uchun ifloslanadi va uni qanday bartaraf etish mumkin?',
                    'youtube_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                    'category_slug': 'suv-ifloslanishi',
                    'author_name': 'Mubina',
                    'author_role': 'Water Conservation Specialist',
                },
                {
                    'title': 'O\'rmonlar yo\'qolishi',
                    'slug': 'ormonlar-kesilishi',
                    'description': 'Daraxtlar nima uchun kesiladi va bu tabiatga qanday zarar keltiradi?',
                    'youtube_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                    'category_slug': 'ormonlar-kesilishi',
                    'author_name': 'Alpamis',
                    'author_role': 'Forest Conservationist',
                },
                {
                    'title': 'Yovvoyi tabiat',
                    'slug': 'yovvoyi-tabiat',
                    'description': 'Yovvoyi tabiatni asrash nimaga muhim?',
                    'youtube_url': 'https://www.youtube.com/embed/dQw4w9WgXcQ',
                    'category_slug': 'yovvoyi-tabiat',
                    'author_name': 'Gulruh',
                    'author_role': 'Wildlife Biologist',
                },
            ]

            for vid_data in videos_data:
                category = Category.objects.get(slug=vid_data.pop('category_slug'))
                video, created = Video.objects.get_or_create(
                    slug=vid_data['slug'],
                    defaults={**vid_data, 'category': category}
                )
                if created:
                    self.stdout.write(f"[+] Created video: {video.title}")

            # Create sample quiz for plastic pollution video
            try:
                plastic_video = Video.objects.get(slug='plastik-ifloslanish')
                quiz, created = Quiz.objects.get_or_create(
                    video=plastic_video,
                    defaults={
                        'title': 'Plastik ifloslanish testi',
                        'passing_score': 70
                    }
                )

                if created:
                    self.stdout.write(f"[+] Created quiz: {quiz.title}")
                    
                    # Question 1
                    q1 = Question.objects.create(
                        quiz=quiz,
                        text='Plastik parchalanishi qancha vaqt oladi?',
                        order=1
                    )
                    Answer.objects.create(question=q1, text='1 yil', is_correct=False)
                    Answer.objects.create(question=q1, text='10 yil', is_correct=False)
                    Answer.objects.create(question=q1, text='100 yil', is_correct=False)
                    Answer.objects.create(question=q1, text='450 yildan ortiq', is_correct=True)
                    
                    # Question 2
                    q2 = Question.objects.create(
                        quiz=quiz,
                        text='Plastik chiqindilarni qanday kamaytirish mumkin?',
                        order=2
                    )
                    Answer.objects.create(question=q2, text='Ko\'proq plastik ishlatish', is_correct=False)
                    Answer.objects.create(question=q2, text='Qayta ishlatiladigan sumkalardan foydalanish', is_correct=True)
                    Answer.objects.create(question=q2, text='Plastikni oqizga tashlash', is_correct=False)
                    Answer.objects.create(question=q2, text='Hech narsa qilmaslik', is_correct=False)
                    
                    # Question 3
                    q3 = Question.objects.create(
                        quiz=quiz,
                        text='Plastik okean hayvonlariga qanday zarar yetkazadi?',
                        order=3
                    )
                    Answer.objects.create(question=q3, text='Zarar yetkazmaydi', is_correct=False)
                    Answer.objects.create(question=q3, text='Ular plastikni yeyishadi va nobud bo\'lishadi', is_correct=True)
                    Answer.objects.create(question=q3, text='Faqat baliqlar zarar ko\'radi', is_correct=False)
                    Answer.objects.create(question=q3, text='Plastik suvda erimaydi', is_correct=False)
                    
                    self.stdout.write("[+] Created 3 quiz questions with answers")
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"[WARNING] Quiz creation skipped: {str(e)}"))

            self.stdout.write(self.style.SUCCESS('[OK] Sample data created successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'[ERROR] Failed to populate data: {str(e)}'))

