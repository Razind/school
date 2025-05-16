--
-- PostgreSQL database dump
--

-- Dumped from database version 16.4 (Debian 16.4-1.pgdg120+1)
-- Dumped by pg_dump version 16.4 (Debian 16.4-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO razind;

--
-- Name: element; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.element (
    id integer NOT NULL,
    section_id integer NOT NULL,
    element_type character varying(50) NOT NULL,
    content text,
    extra_data json,
    "order" integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.element OWNER TO razind;

--
-- Name: element_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.element_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.element_id_seq OWNER TO razind;

--
-- Name: element_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.element_id_seq OWNED BY public.element.id;


--
-- Name: heading; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.heading (
    id integer NOT NULL,
    page_id integer NOT NULL,
    content character varying(255) NOT NULL,
    "order" integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.heading OWNER TO razind;

--
-- Name: heading_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.heading_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.heading_id_seq OWNER TO razind;

--
-- Name: heading_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.heading_id_seq OWNED BY public.heading.id;


--
-- Name: link; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.link (
    id integer NOT NULL,
    page_id integer NOT NULL,
    url character varying(255) NOT NULL,
    title character varying(100) NOT NULL,
    "order" integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.link OWNER TO razind;

--
-- Name: link_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.link_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.link_id_seq OWNER TO razind;

--
-- Name: link_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.link_id_seq OWNED BY public.link.id;


--
-- Name: media; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.media (
    id integer NOT NULL,
    page_id integer NOT NULL,
    file_path character varying(255) NOT NULL,
    file_type character varying(50) NOT NULL,
    "order" integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.media OWNER TO razind;

--
-- Name: media_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.media_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.media_id_seq OWNER TO razind;

--
-- Name: media_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.media_id_seq OWNED BY public.media.id;


--
-- Name: page; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.page (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    slug character varying(100) NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.page OWNER TO razind;

--
-- Name: page_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.page_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.page_id_seq OWNER TO razind;

--
-- Name: page_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.page_id_seq OWNED BY public.page.id;


--
-- Name: post; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.post (
    id integer NOT NULL,
    title character varying(250),
    content character varying(5000),
    date_posted timestamp without time zone,
    image character varying(200)
);


ALTER TABLE public.post OWNER TO razind;

--
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.post_id_seq OWNER TO razind;

--
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.question (
    id integer NOT NULL,
    full_name character varying(100) NOT NULL,
    email character varying(120) NOT NULL,
    question text NOT NULL,
    date_created timestamp without time zone
);


ALTER TABLE public.question OWNER TO razind;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.question_id_seq OWNER TO razind;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: section; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.section (
    id integer NOT NULL,
    page_id integer NOT NULL,
    name character varying(100) NOT NULL,
    "order" integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.section OWNER TO razind;

--
-- Name: section_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.section_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.section_id_seq OWNER TO razind;

--
-- Name: section_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.section_id_seq OWNED BY public.section.id;


--
-- Name: text_block; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public.text_block (
    id integer NOT NULL,
    page_id integer NOT NULL,
    content text NOT NULL,
    "order" integer NOT NULL,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    updated_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.text_block OWNER TO razind;

--
-- Name: text_block_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.text_block_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.text_block_id_seq OWNER TO razind;

--
-- Name: text_block_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.text_block_id_seq OWNED BY public.text_block.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: razind
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    login character varying(50) NOT NULL,
    password_hash character varying(250) NOT NULL,
    date timestamp without time zone
);


ALTER TABLE public."user" OWNER TO razind;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: razind
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO razind;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: razind
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: element id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.element ALTER COLUMN id SET DEFAULT nextval('public.element_id_seq'::regclass);


--
-- Name: heading id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.heading ALTER COLUMN id SET DEFAULT nextval('public.heading_id_seq'::regclass);


--
-- Name: link id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.link ALTER COLUMN id SET DEFAULT nextval('public.link_id_seq'::regclass);


--
-- Name: media id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.media ALTER COLUMN id SET DEFAULT nextval('public.media_id_seq'::regclass);


--
-- Name: page id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.page ALTER COLUMN id SET DEFAULT nextval('public.page_id_seq'::regclass);


--
-- Name: post id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: section id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.section ALTER COLUMN id SET DEFAULT nextval('public.section_id_seq'::regclass);


--
-- Name: text_block id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.text_block ALTER COLUMN id SET DEFAULT nextval('public.text_block_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.alembic_version (version_num) FROM stdin;
4d28f1673cde
\.


--
-- Data for Name: element; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.element (id, section_id, element_type, content, extra_data, "order", created_at, updated_at) FROM stdin;
5	5	image	/static/img/3.jpg	""	2	2025-01-27 12:40:31.616766	2025-01-27 12:40:31.616766
6	6	link	Связаться с нами	"{\\"url\\": \\"mailto:info@example.com\\"}"	1	2025-01-27 12:41:27.618889	2025-01-27 12:41:27.618889
7	7	text	WW	""	1	2025-01-27 17:05:09.394155	2025-01-27 17:05:09.394155
8	8	text	Ghjcnj gtcyz	""	1	2025-01-27 17:05:20.104764	2025-01-27 17:05:25.444815
9	9	text	Rjytw 	""	1	2025-01-27 17:05:34.853276	2025-01-27 17:05:34.853276
4	5	text	Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! Мы лучшая школа! 	""	1	2025-01-27 12:39:19.14593	2025-01-27 20:19:39.222106
10	10	text	ФИО Кадысев: Вячеслав Никалаич\r\nДата рождения: 23.12.2005\r\nммр в доте: 15к	""	1	2025-01-28 18:37:26.844297	2025-01-28 18:37:26.844297
11	11	image	/static/img/3.jpg	""	1	2025-01-28 18:38:07.520377	2025-01-28 18:38:07.520377
12	6	link	Тык	"https://animeru.vip/page-12-918-podnyatiye-urovnya-v-odinochku-2024-onlain-animeru-vse.html"	2	2025-02-02 11:45:12.525	2025-02-02 11:45:12.525
13	6	links_doc	Ну давай давай 	"https://dashboard.render.com/login"	3	2025-02-02 16:00:03.638417	2025-02-02 16:00:03.638417
14	6	links_site	WW	"https://web.telegram.org/k/#-1843435546"	4	2025-02-02 18:38:51.961565	2025-02-02 18:38:51.961565
16	6	links_site	1	"#"	5	2025-02-02 18:57:25.561959	2025-02-02 18:57:25.561959
18	12	links_site	Структура и органы управления образовательной организацией	"#"	2	2025-02-02 19:00:27.236709	2025-02-02 19:00:27.236709
19	12	links_site	Руководство и педагогический состав	{"url": ""}	3	2025-02-02 19:00:49.7849	2025-02-02 19:00:56.01575
20	12	links_site	Документы	{"url": ""}	4	2025-02-02 19:01:12.823382	2025-02-02 19:01:17.485423
21	12	links_site	Образование	"#"	5	2025-02-02 19:01:42.091768	2025-02-02 19:01:42.091768
22	12	links_site	Образовательные стандарты	"#"	6	2025-02-02 19:01:56.501394	2025-02-02 19:01:56.501394
23	12	links_site	Финансово-хозяйственная деятельность	"#"	7	2025-02-02 19:02:42.939214	2025-02-02 19:02:42.939214
24	12	links_site	Материально-техническое обеспечение и оснащённость образовательного процесса	"#"	8	2025-02-02 19:02:56.659259	2025-02-02 19:02:56.659259
25	12	links_site	Платные образовательные услуги	"#"	9	2025-02-02 19:03:12.04833	2025-02-02 19:03:12.04833
26	12	links_site	Вакантные места для приёма (перевода) обучающихся	"#"	10	2025-02-02 19:03:28.248214	2025-02-02 19:03:28.248214
27	12	links_site	Стипендии и меры поддержки обучающихся	"#"	11	2025-02-02 19:03:40.696767	2025-02-02 19:03:40.696767
28	12	links_site	Противодействие коррупции	"#"	12	2025-02-02 19:03:52.827301	2025-02-02 19:03:52.827301
29	12	links_site	Доступная среда	"#"	13	2025-02-02 19:04:06.095405	2025-02-02 19:04:06.095405
30	12	links_doc	Электронные образовательные ресурсы, к которым обеспечивается доступ обучающихся.	"#"	14	2025-02-02 19:04:25.725397	2025-02-02 19:04:25.725397
31	12	links_doc	Порядок текущего контроля успеваемости и промежуточной аттестации обучающихся.	"#"	15	2025-02-02 19:04:38.124161	2025-02-02 19:04:38.124161
32	12	links_doc	Программа повышения объективности проведения всероссийских проверочных работ в МБОУ Школа №70 на 2021-2022 уч.г.	"#"	16	2025-02-02 19:04:52.004084	2025-02-02 19:04:52.004084
33	12	links_doc	Международное сотрудничество - МБОУ Школа №70 г.о. Самара не сотрудничает с международными организациями.	"#"	17	2025-02-02 19:05:17.942235	2025-02-02 19:05:17.942235
34	13	image	/static/img/3.jpg	"/static/img/3.jpg"	1	2025-02-02 19:06:08.290372	2025-02-02 19:06:08.290372
35	12	links_site	Основные сведения	"https://translate.google.com/?sl=ja&tl=ru&text=%E8%A8%80%E8%91%89%E3%81%8C%E3%81%A9%E3%82%8C%E3%81%A0%E3%81%91%E3%81%82%E3%81%A3%E3%81%A6%E3%82%82%E3%80%81%E7%9B%AE%E3%81%AF%E5%98%98%E3%82%92%E3%81%A4%E3%81%8B%E3%81%AA%E3%81%84%E3%81%93%E3%81%A8%E3%82%92%E7%A7%81%E3%81%AF%E7%9F%A5%E3%81%A3%E3%81%A6%E3%81%84%E3%81%BE%E3%81%99%E3%80%82&op=translate"	1	2025-02-13 18:18:23.170625	2025-02-13 18:18:23.170625
\.


--
-- Data for Name: heading; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.heading (id, page_id, content, "order", created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: link; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.link (id, page_id, url, title, "order", created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: media; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.media (id, page_id, file_path, file_type, "order", created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: page; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.page (id, name, slug, created_at, updated_at) FROM stdin;
3	1	11	2025-01-26 22:46:40.149267	2025-01-26 22:53:32.919297
1	2	22	2025-01-26 20:40:57.628003	2025-01-26 22:53:38.608371
5	Главная	home	2025-01-27 12:38:09.692241	2025-01-27 12:38:09.692241
6	FAQ	faq	2025-01-27 17:04:22.321219	2025-01-27 17:04:22.321219
7	Кадысев Вячеслав 	kw	2025-01-28 18:34:54.696165	2025-01-28 18:34:54.696165
4	Сведения об образовательной организации	sooo	2025-01-27 04:39:55.900311	2025-02-02 18:58:00.15522
\.


--
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.post (id, title, content, date_posted, image) FROM stdin;
2	Новый год возможностей в сфере IT стартовал!	Начался набор на учебный год 2024/2025 в Яндекс Лицее. Это отличный шанс для школьников и студентов колледжей в возрасте от 13 до 20 лет прокачать свои навыки программирования и построить карьеру в сфере IT. В программе самое актуальное: изучение Python, Go и Django, промышленная разработка, создание чат-ботов, приложений и других продуктов, машинное обучение.\r\n\r\nДополнительный бонус для выпускников Яндекс Лицея, которые окончат обучение с отличием: до пяти дополнительных баллов при поступлении в ведущие вузы страны, как например, НИУ ВШЭ, ИТМО, ДВФУ, СГУ, ОмГТУ и других.\r\n\r\nДо 9 сентября открыт набор на курсы «Основы программирования на Python» и «Промышленное программирование на Python», до 30 сентября — на годовой онлайн-курс «Программирование на Go», до 24 сентября — на онлайн-специализации.\r\n\r\nУспейте подать заявку: https://clck.ru/JqUQC, на отборочных заданиях вам потребуются базовые знания программирования.\r\n\r\nПодробности на сайте: https://clck.ru/3CuFq2	2024-09-01 11:53:48.005896	e02731bbe4c20e9e2c67d0b4ef3e39.jpg
9	Правила личной безопасности 	На данном изображении представлены правила личной безопасности, которые должен соблюдать каждый!	2024-09-01 11:57:02.028968	39bd90ab487cd4b7caf070d7527114.jpg
8	Творчество для наших мам	fgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fgggggggggggggg	2024-09-01 11:55:37.652196	39a76e61be127bfc2607e6470429d8.jpg
7	Поход в школьный музей 	fgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fgggggggggggggg	2024-09-01 11:55:27.042466	8491380aa8bd69b224c350f25ab227.jpg
5	Правила поведения детей на воде 	fgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fgggggggggggggg	2024-09-01 11:54:51.84716	3d7e6a2d3c025639621d62250a92ce.jpg
4	Правила личной безопасности 	fgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fgggggggggggggg	2024-09-01 11:54:25.02191	a05952640c8ffc4808835d0a2601b4.png
3	Правила личной безопасности 	fgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fggggggggggggggfgggggggggggggg fgggggggggggggg fgggggggggggggg	2024-09-01 11:54:14.784421	d08de33c520a8987b9390df394dacc.png
1	Любимая столовая	пупуру пупуру пупуру пупуру пупуру пупуру пупуру пупуру пупуру 	2024-09-01 06:14:40.169461	d84fcbd5f87d7e11e2bc346a2a31f9.jpg
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.question (id, full_name, email, question, date_created) FROM stdin;
3	Алексей	lehacygankov5@gmail.com	ё12ё12	2025-02-03 10:43:11.284543
\.


--
-- Data for Name: section; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.section (id, page_id, name, "order", created_at, updated_at) FROM stdin;
5	5	О нас	1	2025-01-27 12:38:27.708257	2025-01-27 12:38:27.708257
6	5	Контакты	2	2025-01-27 12:38:35.365998	2025-01-27 12:38:35.365998
7	6	верх	1	2025-01-27 17:04:42.696591	2025-01-27 17:04:42.696591
8	6	центр	2	2025-01-27 17:04:49.915874	2025-01-27 17:04:49.915874
9	6	низ	3	2025-01-27 17:04:57.385492	2025-01-27 17:04:57.385492
10	7	Паспорт	1	2025-01-28 18:35:35.304805	2025-01-28 18:35:35.304805
11	7	Фото	2	2025-01-28 18:35:45.962283	2025-01-28 18:35:45.962283
12	4	Ссылки	1	2025-02-02 18:59:03.611535	2025-02-02 18:59:03.611535
13	4	Фото	2	2025-02-02 19:05:42.103942	2025-02-02 19:05:42.103942
\.


--
-- Data for Name: text_block; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public.text_block (id, page_id, content, "order", created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: razind
--

COPY public."user" (id, login, password_hash, date) FROM stdin;
1	admin	scrypt:32768:8:1$kiYIC0V456d9X5Hx$c735a8ffdd0d365bed13bb971e73b51cbf70b899897d51578db9017e3b793c9f1b422c309c7a7a4cfebcbe4193f1c543057033375931c62dee12734242345c4d	2024-09-01 06:13:30.023742
\.


--
-- Name: element_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.element_id_seq', 35, true);


--
-- Name: heading_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.heading_id_seq', 1, false);


--
-- Name: link_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.link_id_seq', 1, false);


--
-- Name: media_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.media_id_seq', 1, false);


--
-- Name: page_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.page_id_seq', 7, true);


--
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.post_id_seq', 12, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.question_id_seq', 3, true);


--
-- Name: section_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.section_id_seq', 13, true);


--
-- Name: text_block_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.text_block_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: razind
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: element element_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.element
    ADD CONSTRAINT element_pkey PRIMARY KEY (id);


--
-- Name: heading heading_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.heading
    ADD CONSTRAINT heading_pkey PRIMARY KEY (id);


--
-- Name: link link_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.link
    ADD CONSTRAINT link_pkey PRIMARY KEY (id);


--
-- Name: media media_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.media
    ADD CONSTRAINT media_pkey PRIMARY KEY (id);


--
-- Name: page page_name_key; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.page
    ADD CONSTRAINT page_name_key UNIQUE (name);


--
-- Name: page page_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.page
    ADD CONSTRAINT page_pkey PRIMARY KEY (id);


--
-- Name: page page_slug_key; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.page
    ADD CONSTRAINT page_slug_key UNIQUE (slug);


--
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- Name: question question_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (id);


--
-- Name: section section_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.section
    ADD CONSTRAINT section_pkey PRIMARY KEY (id);


--
-- Name: text_block text_block_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.text_block
    ADD CONSTRAINT text_block_pkey PRIMARY KEY (id);


--
-- Name: user user_login_key; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_login_key UNIQUE (login);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: element element_section_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.element
    ADD CONSTRAINT element_section_id_fkey FOREIGN KEY (section_id) REFERENCES public.section(id);


--
-- Name: heading heading_page_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.heading
    ADD CONSTRAINT heading_page_id_fkey FOREIGN KEY (page_id) REFERENCES public.page(id);


--
-- Name: link link_page_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.link
    ADD CONSTRAINT link_page_id_fkey FOREIGN KEY (page_id) REFERENCES public.page(id);


--
-- Name: media media_page_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.media
    ADD CONSTRAINT media_page_id_fkey FOREIGN KEY (page_id) REFERENCES public.page(id);


--
-- Name: section section_page_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.section
    ADD CONSTRAINT section_page_id_fkey FOREIGN KEY (page_id) REFERENCES public.page(id);


--
-- Name: text_block text_block_page_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: razind
--

ALTER TABLE ONLY public.text_block
    ADD CONSTRAINT text_block_page_id_fkey FOREIGN KEY (page_id) REFERENCES public.page(id);


--
-- PostgreSQL database dump complete
--

