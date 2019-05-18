# IAM Lab website

This website is built in Hugo using the [Academic Kickstart](https://sourcethemes.com/academic/) template. Check the [docs](https://sourcethemes.com/academic/docs/page-builder/) if you want to add new modules or update the template. The source code is hosted on the IAM Lab GitHub organisation. The compiled website is hosted on Netlify with continuous integration, Simon will have the password to the Netlify account in case you need to see the deployment logs if one of your git push broke the website.

## Before adding an image
Optimise any image to keep the website light and fast using [https://bulkresizephotos.com](https://bulkresizephotos.com). Choose your image, and got to `File Size` choosing a max File image of 100kb. You can also use that website to resize your photos.

## Correct typos

You can use GitHub's GUI to correct any typos. Go to the file you want to modify, for example, [Alan's profile](https://github.com/IAM-lab/website_iam/blob/master/content/authors/Alan-Davies/_index.md) and click on the pencil icon. Once any changes are done, add a commit **title** (for example, "Add new affiliation for Alan") and optionally a **description**, then click _Commit changes_. The site will deploy itself, and you should see your changes online within ~30 sec.

## Add/Modify/Delete new people, project, sections, news

**First, you need to set up your dev environment:**

1. `git clone https://github.com/IAM-lab/website_iam.git iam_website`
2. `cd iam_website`
3. `git submodule update --init --recursive`
4. `git pull`
5. Download [Hugo Extended](https://github.com/gohugoio/hugo/releases) version for your platform and copy the relevant binary to the root of your `iam_website` folder
6. Run `hugo serve` at the root level of `iam_website`, if everything went well you should see the website in [localhost:1313](http://localhost:1313)

Once you have made any changes outlined below, submit them to the repo, and they will be automatically deployed:

1. `git add .`
2. `git commit -m "MEANINGFUL message please"`
3. `git push`

### Add People

1. Go to `iam_website/content/authors`
2. Copy `Julio-Vega` folder and paste it with the name of the new person, _replace spaces with dashes_ (for example `Jane-Doe`).
3. Change:
   -  `name`
   -  `authors` (this value has to match the folder name without dashes)
   -  leave `superuser` as false
   -  `role`
   -  `organizations`
   -  `bio` (1 or 2 sentences)
   -  `interests` (keywords)
   -  `education`
   -  `social links` (you can use [font awesome icons](https://fontawesome.com/icons?d=gallery) but be careful to choose the right `icon pack`)
   -  ignore `email`
   -  `user_groups` accordingly to the group you want this person to belong to in People (to see all available groups see `user_groups` in `content/home/people.md`)
4.  Add a profile image named `avatar.png` or `avatar.jpg` to this person's folder.
5.  At the end your file structure should be something like:
    - `content/authors/Jane-Doe/_index.md`
    - `content/authors/Jane-Doe/avatar.jpg`

### Modify People

Just modify their `_index.md` file.

### Delete People

Just delete their folder.

### Add Projects

1. In your `iam_website` folder execute `hugo new  --kind project project/my-project-name`
2. Just as with people, edit the newly created file `content/project/my-project-name.md`.
3. If you want to link a project to people in the lab, add a field `authors` within the two `+++`. For example `authors = ["Jonathan Carlton", "Andy Brown", "Caroline Jay"]`
4. You can link the project to an external project website by setting the `external_link: "http://external-project.com"` variable (our internal page won't be shown tho')
5. You can add a project image named `featured.png` or `featured.jpg` to this project's folder.
6.  You can add a longer project description below the final `+++`.

### Modify Projects

Just modify its `index.md` file.

### Delete Projects

Just delete its folder.

### Add News

1. In your `iam_website` folder execute `hugo new  --kind post post/my-article-name`
2. You can add a news image named `featured.png` or `featured.jpg` to this news' folder.
3. Feel free to add `tags` and `categories`  to its `index.md` file. The former will show up in the lab's world cloud, and the latter function as filters (try going to `cs.iam-lab/categories/your-category`)
4. Make sure you link your news to a project by setting `projects = ["project-folder"]`

### Modify News
Just modify its `index.md` file.

### Delete News

Just delete its folder.

### Add Publications

There are two ways of adding publications, one for permanent staff and one for the rest.

For permanent staff add to `bibliography/dblp-ids.txt` their [dblp PID resource URI](https://dblp.uni-trier.de/faq/17334565.html) with a `.bib.` extension followed by a pipe `|` followed by their name as it appears in their publications: `https://dblp.org/pid/h/SimonHarper.bib|Simon Harper`. I created a python script `download_bib.py` that will take those URIs and download the respective bib files. We use the name after `|` to get rid of bib entries that are crossref entries (entries with conference proceedings info instead of personal publications). Why do we use dblp? Because it exposes curated bib files for free and without restrictions, having consistent bib keys allows us to ignore duplicates automatically.

For non-permanent people (e.g. PhD students) it is best to add individual bib files to the folder `bibliography/bib`. **Be careful with duplicates**, the website won't detect if two papers are the same if they have different bib keys. This option is ideal for adding a bunch of specific papers not indexed by dblp or not co-authored by permanent staff.

In any case, `download_bib.py` will read the dblp URIs and the individual bib files and will execute [Academic Admin](https://github.com/sourcethemes/academic-admin) to import all the bib entries automatically.

The `download_bib.py` is executed in Netlify servers every time there's a push to the website git repo. This is configured in line 2 of `netlify.toml`, while Academic Admin is specified in `requirements.txt`, and the python version in `runtime.txt`.

### Modify Publications

If you want to modify papers downloaded automatically from dblp, you would need to modify the parsed bib entry after line 29 of `download_bib.py` before it is appended to `db.entries`. If you want to modify papers of non-permanent staff just change the entry in the individual bib files in `bibliography/bib`.

### Delete Publications

If you want to get rid of specific papers downloaded from dblp, add their bibkeys to `ignore_files_from_dblp` in line 13 of `download_bib.py`. If you want to get rid of papers of non-permanent staff, just delete the entry in the individual bib files in `bibliography/bib`.