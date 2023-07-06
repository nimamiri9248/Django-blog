from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class PostSerializer(serializers.ModelSerializer):
    # title=serializers.CharField(max_length=100)

    # make a field readonly

    author = serializers.ReadOnlyField()
    # content=serializers.charField(read_only=True)
    # read_only_fields = ['author']

    snippet = serializers.ReadOnlyField(source="get_snippet")

    url = serializers.SerializerMethodField()

    # getting category name instead of id

    category = serializers.SlugRelatedField(
        slug_field="name",
        read_only=False,
        many=False,
        queryset=Category.objects.all(),
    )

    def get_url(self, obj):
        request = self.context.get("request")
        absolute_url = obj.get_absolute_url()
        return request.build_absolute_uri(absolute_url)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "image",
            "author",
            "snippet",
            "content",
            "url",
            "category",
            "status",
        )

    # overring the representation of the list
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["state"] = "list"
        request = self.context.get("request")
        if request.parser_context["kwargs"].get("pk"):
            rep.pop("snippet", None)
            rep.pop("url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    # def create(self, validated_data):
    #     validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
    #     return super().create(validated_data)
