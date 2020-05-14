-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 14, 2020 at 12:56 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mentorski`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add custom user', 1, 'add_customuser'),
(2, 'Can change custom user', 1, 'change_customuser'),
(3, 'Can delete custom user', 1, 'delete_customuser'),
(4, 'Can view custom user', 1, 'view_customuser'),
(5, 'Can add log entry', 2, 'add_logentry'),
(6, 'Can change log entry', 2, 'change_logentry'),
(7, 'Can delete log entry', 2, 'delete_logentry'),
(8, 'Can view log entry', 2, 'view_logentry'),
(9, 'Can add permission', 3, 'add_permission'),
(10, 'Can change permission', 3, 'change_permission'),
(11, 'Can delete permission', 3, 'delete_permission'),
(12, 'Can view permission', 3, 'view_permission'),
(13, 'Can add group', 4, 'add_group'),
(14, 'Can change group', 4, 'change_group'),
(15, 'Can delete group', 4, 'delete_group'),
(16, 'Can view group', 4, 'view_group'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add predmeti', 7, 'add_predmeti'),
(26, 'Can change predmeti', 7, 'change_predmeti'),
(27, 'Can delete predmeti', 7, 'delete_predmeti'),
(28, 'Can view predmeti', 7, 'view_predmeti'),
(29, 'Can add upisi', 8, 'add_upisi'),
(30, 'Can change upisi', 8, 'change_upisi'),
(31, 'Can delete upisi', 8, 'delete_upisi'),
(32, 'Can view upisi', 8, 'view_upisi');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(2, 'admin', 'logentry'),
(4, 'auth', 'group'),
(3, 'auth', 'permission'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(1, 'users', 'customuser'),
(7, 'users', 'predmeti'),
(8, 'users', 'upisi');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'users', '0001_initial', '2020-03-16 15:18:26.501417'),
(2, 'contenttypes', '0001_initial', '2020-03-16 15:18:26.563926'),
(3, 'admin', '0001_initial', '2020-03-16 15:18:26.595166'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-03-16 15:18:26.735786'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-03-16 15:18:26.735786'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-03-16 15:18:26.829549'),
(7, 'auth', '0001_initial', '2020-03-16 15:18:26.938921'),
(8, 'auth', '0002_alter_permission_name_max_length', '2020-03-16 15:18:27.251409'),
(9, 'auth', '0003_alter_user_email_max_length', '2020-03-16 15:18:27.282660'),
(10, 'auth', '0004_alter_user_username_opts', '2020-03-16 15:18:27.282660'),
(11, 'auth', '0005_alter_user_last_login_null', '2020-03-16 15:18:27.298283'),
(12, 'auth', '0006_require_contenttypes_0002', '2020-03-16 15:18:27.298283'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2020-03-16 15:18:27.298283'),
(14, 'auth', '0008_alter_user_username_max_length', '2020-03-16 15:18:27.313910'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2020-03-16 15:18:27.313910'),
(16, 'auth', '0010_alter_group_name_max_length', '2020-03-16 15:18:27.345157'),
(17, 'auth', '0011_update_proxy_permissions', '2020-03-16 15:18:27.345157'),
(18, 'sessions', '0001_initial', '2020-03-16 15:18:27.376405'),
(19, 'users', '0002_auto_20200315_2233', '2020-03-16 15:35:47.626074'),
(20, 'users', '0003_customuser_username1', '2020-03-16 15:35:47.632581'),
(21, 'users', '0004_auto_20200316_1618', '2020-03-16 15:35:47.632581'),
(22, 'users', '0005_auto_20200316_1846', '2020-03-16 17:46:22.026956'),
(23, 'users', '0006_auto_20200408_1509', '2020-04-08 13:09:49.485777'),
(24, 'users', '0007_auto_20200408_1531', '2020-04-08 13:31:20.886182'),
(25, 'users', '0008_auto_20200411_1432', '2020-04-11 12:32:09.700902'),
(26, 'users', '0009_auto_20200501_1501', '2020-05-01 13:01:24.855855'),
(27, 'users', '0010_auto_20200501_1502', '2020-05-01 13:02:15.419058'),
(28, 'users', '0011_auto_20200501_1854', '2020-05-01 16:54:55.615832');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('cvaf9fmyzro2o9x1x9jj8wbe2jou16pa', 'Y2U1YmE3MzVkZjkyNTZjZDBmYzUyZmE0YTZjNzU4ZGFiZDEzOTk3MDp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZjM4Y2ZmNzkxMDYwOTk1MDA0Y2I2MmVjMDIzOGIwZWU3NTQxYjI3In0=', '2020-05-18 15:31:04.893168'),
('e82dx56mrh8as2ztdup943ohhc3m9xl7', 'MjI0MDk2ZjA0NjdjMWExOGZjN2FiYzFmNmE0OGE5NzBhMjQzMGRiNTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwOTkwODNhOWYyZjQ3ZjExYzJhNWY1NTk0OGUwN2E1YWM5NGZlMjQwIn0=', '2020-04-22 15:01:50.388280');

-- --------------------------------------------------------

--
-- Table structure for table `korisnici`
--

CREATE TABLE `korisnici` (
  `id` int(11) NOT NULL,
  `email` varchar(55) NOT NULL,
  `password` varchar(128) NOT NULL,
  `role` enum('mentor','student') NOT NULL,
  `status` enum('none','redovni','izvanredni') NOT NULL,
  `username` varchar(30) CHARACTER SET utf8mb4 NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `korisnici`
--

INSERT INTO `korisnici` (`id`, `email`, `password`, `role`, `status`, `username`, `date_joined`, `last_login`, `is_staff`, `is_active`, `is_superuser`) VALUES
(1, 'mentor@oss.hr', 'pbkdf2_sha256$180000$6yo9QbQfQ8tM$eegdAUPVP5VRMZTg1wSfHaeI230N2GNRs+HCQjW7/RA=', 'mentor', 'none', '', '2020-03-25 14:35:46.164429', '2020-03-25 14:48:18.577772', 0, 1, 0),
(2, 'red@oss.hr', 'pbkdf2_sha256$180000$QebKfC9uEmrA$tEPj0mJ6h9AHgPDd9xdyMkWYcsFF0Vp/JcTSKTv+5L8=', 'student', 'redovni', '', '2020-03-25 14:36:55.343770', '2020-03-25 14:36:55.343770', 0, 1, 0),
(3, 'izv@oss.hr', 'pbkdf2_sha256$180000$TUHUMENySjuc$YbM42YEakgDc9jM1DM+RBiiY37qpYE88eM34C0hlJNQ=', 'student', 'izvanredni', '', '2020-03-25 14:38:12.772786', '2020-05-03 20:39:58.753712', 0, 1, 0),
(4, 'kraljevic_marko@hotmail.com', 'pbkdf2_sha256$180000$m5iNa2kMgSP0$ulvKZlwTJlhrtp7LqW+m5NbTw8iq8sabedyh1Rh2F7Y=', 'mentor', 'redovni', '', '2020-03-23 17:27:19.559260', '2020-05-04 15:31:04.890131', 1, 1, 1),
(5, 'red1@oss.hr', 'pbkdf2_sha256$180000$kDVxUDp9eDBV$qvvCX1xfEXEsXikpscpBHBgIa/NHK4mr6OwAy7VQpek=', 'student', 'redovni', '', '2020-04-02 12:41:20.040610', '2020-04-02 12:41:20.040610', 0, 1, 0),
(6, 'red2@oss.hr', 'pbkdf2_sha256$180000$6tmKysUeumS0$tUDmyJZytKWcXYREMKMmcBhQNDCHw6MGSL4aQ3ntsAk=', 'student', 'redovni', '', '2020-04-02 12:41:43.184364', '2020-04-02 12:41:43.184364', 0, 1, 0),
(7, 'redovni3@oss.hr', 'pbkdf2_sha256$180000$6uUCJdY0hXrR$fb3SoNYHGadfSz1Hic+RqQNUcWC3wjIjx8yCkVikg20=', 'student', 'redovni', '', '2020-04-02 12:42:27.786803', '2020-04-02 12:42:27.786803', 0, 1, 0),
(8, 'red4@oss.hr', 'pbkdf2_sha256$180000$ibkGcEZ6kqNT$IR8WFYIbuIUsnDe7J8FlJ/BYP5Yokb1fHsR8Pv3kams=', 'student', 'redovni', '', '2020-04-02 12:42:58.901116', '2020-04-02 12:42:58.901116', 0, 1, 0),
(9, 'red5@oss.hr', 'pbkdf2_sha256$180000$428UKzquAsVV$GGTIhBAfjAchb0/23B9Ey1vzUKXAaeW6gxMTuniNtEk=', 'student', 'redovni', '', '2020-04-02 12:43:38.460506', '2020-04-02 12:43:38.460506', 0, 1, 0),
(10, 'redovni6@oss.hr', 'pbkdf2_sha256$180000$cZhsQMOMoNzE$zoQkmWZcgEjnRP67R53KOgvcDsOoYcx7oc+mUgXNHxc=', 'student', 'redovni', '', '2020-04-02 12:43:57.418816', '2020-04-02 12:43:57.419813', 0, 1, 0),
(11, 'rred8@oss.hr', 'pbkdf2_sha256$180000$aT3SGcpgbudy$pXPLqSaJbMAZzmC9nmCO7RHTI/Y9u5yTIPcwoXxbM6U=', 'student', 'redovni', '', '2020-04-02 12:44:32.573715', '2020-04-02 12:44:32.573715', 0, 1, 0),
(12, 'izv1@oss.hr', 'pbkdf2_sha256$180000$KXBKiAtO5Tcw$Qd/2je4hu5nXDNo/DYRN2uhg7u6CLoOMimcv3o2xNSg=', 'student', 'izvanredni', '', '2020-04-02 14:20:56.860069', '2020-04-13 15:00:55.157935', 0, 1, 0),
(13, 'red9@oss.hr', 'pbkdf2_sha256$180000$LtfRyUOqUyQJ$+t3hAKbt5MEjKi4hEDplxUxVvHHs0r7kPe03fjuWj0I=', 'student', 'redovni', '', '2020-04-02 14:21:34.333935', '2020-04-02 14:21:34.333935', 0, 1, 0),
(14, 'izv2@oss.hr', 'pbkdf2_sha256$180000$P1hh9eQpARlw$tZCiTN/lF3AXS3ZssAaLVmCa2L4ZYxMzFVT0HjuSI5c=', 'student', 'izvanredni', '', '2020-04-02 14:39:59.800608', '2020-04-02 14:39:59.800608', 0, 1, 0),
(15, 'izv4@oss.hr', 'pbkdf2_sha256$180000$SlJpD3l2ON94$JpsttNwVZfvA7xmpGNZ+7Yu8ladaNOUqJBZJw561Ewo=', 'student', 'izvanredni', '', '2020-04-02 14:40:16.559274', '2020-04-02 14:40:16.559274', 0, 1, 0),
(16, 'izv5@oss.hr', 'pbkdf2_sha256$180000$8hcVPxA6QBEd$a9MINCiG0rZBLaLh71nLaZvoUXy/VQ5LUDbfiWSMROw=', 'student', 'izvanredni', '', '2020-04-02 14:40:29.768629', '2020-04-02 14:40:29.768629', 0, 1, 0),
(17, 'izv6@oss.hr', 'pbkdf2_sha256$180000$aBChyAGS8p1b$DT7D1yupJz0yJdOkd/QZsghOHhsmZLCZHhQVWghHIt0=', 'student', 'izvanredni', '', '2020-04-02 14:40:42.670095', '2020-04-02 14:40:42.670095', 0, 1, 0),
(18, 'izv7@oss.hr', 'pbkdf2_sha256$180000$XmLvAlU8JeHF$ip2sX+SvLTAq+AtwXEpz4kUB1LI/LJTyHPpNU9avOWY=', 'student', 'izvanredni', '', '2020-04-02 14:41:27.870121', '2020-04-02 14:41:27.870121', 0, 1, 0),
(19, 'izv10@oss.hr', 'pbkdf2_sha256$180000$6zPfVa0EM2BD$qLm6Wy1k7uWQ9NQjHy/f8Eqsa+aZRkuwMy+YgPmnmb8=', 'student', 'izvanredni', '', '2020-04-02 14:56:32.203434', '2020-04-02 14:56:32.203434', 0, 1, 0),
(20, 'izv99@oss.hr', 'pbkdf2_sha256$180000$OjWnuVh5lDLW$vqqvezjmgOK2sDHofhAUbDeHUPHOHi9i9eYIIEgu4cY=', 'student', 'izvanredni', '', '2020-05-03 15:29:53.911243', '2020-05-03 15:30:04.009072', 0, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `predmeti`
--

CREATE TABLE `predmeti` (
  `id` int(11) NOT NULL,
  `ime` varchar(255) NOT NULL,
  `kod` varchar(16) NOT NULL,
  `program` text NOT NULL,
  `bodovi` int(11) DEFAULT NULL,
  `sem_redovni` int(11) DEFAULT NULL,
  `sem_izvanredni` int(11) DEFAULT NULL,
  `izborni` enum('da','ne') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `predmeti`
--

INSERT INTO `predmeti` (`id`, `ime`, `kod`, `program`, `bodovi`, `sem_redovni`, `sem_izvanredni`, `izborni`) VALUES
(1, 'Linearna algebra', 'SIT001', 'Program nije unesen', 6, 1, 1, 'ne'),
(2, 'Fizika', 'SIT002', 'Program nije unesen', 6, 1, 3, 'ne'),
(3, 'Osnove elektronike', 'SIT003', 'Program nije unesen', 6, 1, 1, 'ne'),
(4, 'Digitalna i mikroprocesorska tehnika', 'SIT004', 'Program nije unesen', 7, 1, 2, 'ne'),
(6, 'Engleski jezik 1', 'SIT006', 'Program nije unesen', 2, 1, 1, 'ne'),
(7, 'Analiza 1', 'SIT007', 'Program nije unesen', 7, 2, 2, 'ne'),
(8, 'Osnove elektronike', 'SIT008', 'Program nije unesen', 6, 2, 2, 'ne'),
(9, 'Arhitektura i organizacija digitalnih računala', 'SIT009', 'Program nije unesen', 7, 2, 3, 'ne'),
(10, 'Uvod u programiranje', 'SIT010', 'Program nije unesen', 8, 2, 3, 'ne'),
(11, 'Engleski jezik 2', 'SIT011', 'Program nije unesen', 2, 2, 2, 'ne'),
(12, 'Primijenjena i numerička matematika', 'SIT012', 'Program nije unesen', 6, 3, 4, 'ne'),
(13, 'Programske metode i apstrakcije', 'SIT013', 'Program nije unesen', 8, 3, 4, 'ne'),
(14, 'Baze podataka', 'SIT014', 'Program nije unesen', 6, 3, 5, 'ne'),
(15, 'Informacijski sustavi', 'SIT015', 'Program nije unesen', 6, 3, 4, 'ne'),
(16, 'Tehnički Engleski jezik', 'SIT016', 'Program nije unesen', 4, 3, 5, 'ne'),
(17, 'Računalne mreže', 'SIT017', 'Program nije unesen', 5, 4, 5, 'ne'),
(18, 'Operacijski sustavi', 'SIT018', 'Program nije unesen', 5, 4, 5, 'ne'),
(19, 'Strukture podataka i algoritmi', 'SIT019', 'Program nije unesen', 5, 4, 6, 'da'),
(20, 'Objektno programiranje', 'SIT020', 'Program nije unesen', 5, 4, 6, 'da'),
(21, 'Baze podataka 2', 'SIT021', 'Program nije unesen', 5, 4, 6, 'da'),
(22, 'Mrežne usluge i programiranje', 'SIT022', 'Program nije unesen', 5, 4, 6, 'da'),
(23, 'Arhitektura osobnih računala', 'SIT023', 'Program nije unesen', 5, 4, 6, 'da'),
(24, 'Projektiranje i upravljanje računalnim mrežama', 'SIT024', 'Program nije unesen', 5, 4, 6, 'da'),
(25, 'Projektiranje informacijskih sustava', 'SIT025', 'Program nije unesen', 5, 4, 6, 'da'),
(26, 'Informatizacija poslovanja', 'SIT026', 'Program nije unesen', 5, 4, 6, 'da'),
(27, 'Ekonomika i organizacija poduzeća', 'SIT027', 'Program nije unesen', 2, 5, 7, 'ne'),
(28, 'Analiza 2', 'SIT028', 'Program nije unesen', 6, 5, 7, 'ne'),
(29, 'Industrijska praksa', 'SIT029', 'Program nije unesen', 2, 5, 7, 'ne'),
(30, 'Arhitektura poslužiteljskih računala', 'SIT030', 'Program nije unesen', 5, 5, 7, 'da'),
(31, 'Sigurnost računala i podataka', 'SIT031', 'Program nije unesen', 5, 5, 7, 'da'),
(32, 'Programski alati na UNIX računalima', 'SIT032', 'Program nije unesen', 5, 5, 7, 'da'),
(33, 'Napredno Windows programiranje', 'SIT033', 'Program nije unesen', 5, 5, 7, 'da'),
(34, 'Objektno orijentirano modeliranje', 'SIT034', 'Program nije unesen', 5, 5, 7, 'da'),
(35, 'Programiranje u Javi', 'SIT035', 'Program nije unesen', 5, 5, 7, 'da'),
(36, 'Programiranje na Internetu', 'SIT036', 'Program nije unesen', 5, 5, 7, 'da'),
(37, 'Elektroničko poslovanje', 'SIT037', 'Program nije unesen', 5, 5, 7, 'da'),
(38, 'Diskretna matematika', 'SIT038', 'Program nije unesen', 6, 6, 8, 'ne'),
(39, 'Upravljanje poslužiteljskim računalima', 'SIT039', 'Program nije unesen', 5, 6, 8, 'da'),
(40, 'Programiranje u C#', 'SIT040', 'Program nije unesen', 5, 6, 8, 'da'),
(41, 'Društveni informacijski sustavi', 'SIT041', 'Program nije unesen', 5, 6, 8, 'da'),
(42, 'Oblikovanje Web stranica', 'SIT042', 'Program nije unesen', 5, 6, 8, 'da'),
(43, 'Vođenje projekata i dokumentacija', 'SIT043', 'Program nije unesen', 5, 6, 8, 'da'),
(44, 'Informatizacija proizvodnje', 'SIT044', 'Program nije unesen', 5, 6, 8, 'da'),
(45, 'Analiza i obrada podataka', 'SIT045', 'Program nije unesen', 5, 6, 8, 'da'),
(46, 'Njemački jezik', 'SSZP40', 'Program nije unesen', 4, 6, 8, 'da'),
(47, 'Talijanski jezik', 'SSZP50', 'Program nije unesen', 4, 6, 8, 'da'),
(48, 'Završni rad', 'SIT046', 'Program nije unesen', 8, 6, 8, 'ne');

-- --------------------------------------------------------

--
-- Table structure for table `upisi`
--

CREATE TABLE `upisi` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `predmet_id` int(11) NOT NULL,
  `status` enum('polozen','nepolozen') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `upisi`
--

INSERT INTO `upisi` (`id`, `student_id`, `predmet_id`, `status`) VALUES
(1, 3, 21, 'nepolozen'),
(2, 12, 7, 'polozen'),
(9, 12, 11, 'nepolozen'),
(10, 12, 16, 'nepolozen'),
(12, 15, 9, 'nepolozen'),
(13, 16, 6, 'nepolozen'),
(14, 16, 11, 'nepolozen'),
(15, 16, 10, 'nepolozen'),
(16, 16, 7, 'nepolozen'),
(17, 16, 18, 'nepolozen'),
(18, 16, 48, 'nepolozen'),
(23, 13, 9, 'nepolozen'),
(24, 13, 14, 'nepolozen'),
(69, 14, 1, 'nepolozen'),
(75, 12, 10, 'nepolozen'),
(85, 5, 3, 'polozen'),
(88, 2, 2, 'polozen'),
(91, 2, 17, 'nepolozen'),
(93, 2, 7, 'polozen'),
(95, 3, 9, 'nepolozen'),
(96, 2, 12, 'nepolozen'),
(97, 2, 4, 'nepolozen');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `korisnici`
--
ALTER TABLE `korisnici`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `predmeti`
--
ALTER TABLE `predmeti`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `kod` (`kod`);

--
-- Indexes for table `upisi`
--
ALTER TABLE `upisi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `predmet_id` (`predmet_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `korisnici`
--
ALTER TABLE `korisnici`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `predmeti`
--
ALTER TABLE `predmeti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `upisi`
--
ALTER TABLE `upisi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `upisi`
--
ALTER TABLE `upisi`
  ADD CONSTRAINT `upisi_predmet_id_ecb62bfe_fk_predmeti_id` FOREIGN KEY (`predmet_id`) REFERENCES `predmeti` (`id`),
  ADD CONSTRAINT `upisi_student_id_ea6bf88b_fk_korisnici_id` FOREIGN KEY (`student_id`) REFERENCES `korisnici` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
