# eminA API

An eminA API is a powerful tool for developers who want to create software related to anime. It provides access to a vast database of anime information, including titles, synopsis, genres, ratings,reviews, and more. With an eminA API, developers can create applications.


## Documentation
Hello for more details you can look for the auto-generated documentation provides for fast-api you can access typing `/docs` on the url like this:


```http
    https://anime-api-production-cc78.up.railway.app/docs 
```

## API Reference

#### Get all animes


```http
  GET ~/
```

##### Response body - **Example response**
```json
[
    {
        "synopsis": "Barely surviving in a barrel after passing through a terrible whirlpool at sea, carefree Monkey D. Luffy ends up aboard a ship under attack by fearsome pirates. Despite being a naive-looking teenager, he is not to be underestimated. Unmatched in battle, Luffy is a pirate himself who resolutely pursues the coveted One Piece treasure and the King of the Pirates title that comes with it.",
        "editor": "TOEI Animation",
        "genres": "action,adventure,fantasy,shounen",
        "aired": true,
        "reviews": 990,
        "anime_name": "One piece",
        "id": 1,
        "rate": 4.9,
        "episodes": 1076,
        "year_release": 1999,
        "images": "https://i.imgur.com/HJd2iHi.jpg"
    },
    {
        "synopsis": "The seemingly unimpressive Saitama has a rather unique hobby: being a hero. In order to pursue his childhood dream, Saitama relentlessly trained for three years, losing all of his hair in the process. Now, Saitama is so powerful, he can defeat any enemy with just one punch. However, having no one capable of matching his strength has led Saitama to an unexpected problem—he is no longer able to enjoy the thrill of battling and has become quite bored.",
        "editor": "Madhouse",
        "genres": "Action,Comedy,Superhero",
        "aired": false,
        "reviews": 508,
        "anime_name": "One Punch Man",
        "id": 2,
        "rate": 4.8,
        "episodes": 12,
        "year_release": 2015,
        "images": "https://i.imgur.com/k0lqQZe.jpg"
    },
    {
        "synopsis": "After death, either Heaven or Hell awaits most humans. But for a select few, death brings them to Quindecim—a bar where only pairs of people who die at the same time can enter. Attending the bar is an enigmatic figure known as Decim, who also acts as the arbiter. He passes judgment on those who wind up at Quindecim by challenging them to a life-threatening game. These games determine if the patron's soul will reincarnate into a new life, or be sent into the void, never to be seen again.",
        "editor": " Madhouse",
        "genres": "Drama,Supernatural,Suspense",
        "aired": true,
        "reviews": 446,
        "anime_name": "Death Parade",
        "id": 3,
        "rate": 4.7,
        "episodes": 12,
        "year_release": 2015,
        "images": "https://i.imgur.com/uxy7gSD.jpg"
    },
    {
        "synopsis": "With the appearance of a mysterious virus that kills everyone above the age of 13, mankind becomes enslaved by previously hidden, power-hungry vampires who emerge in order to subjugate society with the promise of protecting the survivors, in exchange for donations of",
        "editor": "Wit Studio",
        "genres": "Action,Drama,Supernatural",
        "aired": false,
        "reviews": 194,
        "anime_name": "Owari no Seraph",
        "id": 4,
        "rate": 4.7,
        "episodes": 12,
        "year_release": 2015,
        "images": "https://i.imgur.com/CN56ogL.jpg"
    }
]
```
#### Get an anime

```http
  GET ~/anime/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. anime `id`|


#### Get animes by query

`genres` Can recieve more than 1 genre, have to be separed by a dash `-`
    
`year` It receives a year and cannot be greater than the actual year 

```http
  GET /animes/?genre=action&year=2015
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `genre - year`      | `string - Integer` | Both querys are optional.|

#### Post and anime

```http
  POST ~/anime
```

`id` is not requiered because is auto-incremental 
`genres` Have to be separed by a `-` like the example 


If everythin goes okay you will recive a `status code - 200` with the followed message `"Anime has been registered successfully"`

##### Request body example
```json 
{
    "synopsis": "Barely surviving in a barrel after passing through a terrible whirlpool at sea, carefree Monkey D. Luffy ends up aboard a ship under attack by fearsome pirates. Despite being a naive-looking teenager, he is not to be underestimated. Unmatched in battle, Luffy is a pirate himself who resolutely pursues the coveted One Piece treasure and the King of the Pirates title that comes with it.",
    "editor": "TOEI Animation",
    "genres": "action-adventure-fantasy-shounen",
    "aired": true,
    "reviews": 990,
    "anime_name": "One piece",
    "rate": 4.9,
    "episodes": 1076,
    "year_release": 1999,
    "images": "https://i.imgur.com/HJd2iHi.jpg"
}
```


#### Delete an anime

```http
  DELETE ~/anime/${id}
```
If you want to delete an anime you will need to specify in headers request the **jwt token** 

`status code - 200` You'll going to recive this message ```"Anime has been deleted succefully"```

`status code - 404` You'll recive the followed message ```"Anime not found"```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. anime `id` to delete |


#### Update an anime

```http
  PUT ~/anime/${id}
```
If you want to update an anime you will need to specify in headers the **jwt token** 

`status code - 200` You'll going to recive this message ```"Anime has been modified succefully"```

`status code - 404` You'll recive the followed message ```"Anime not found"```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required** anime `id`  to update |


##### Request body
```json
{
  "id": 0,
  "anime_name": "string",
  "rate": 5,
  "synopsis": "string",
  "reviews": 0,
  "editor": "string",
  "episodes": 0,
  "genres": "action-adventure",
  "aired": true,
  "year_release": 2023,
  "images": "Url image"
}
```
