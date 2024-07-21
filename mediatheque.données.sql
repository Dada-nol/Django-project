-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : sam. 20 juil. 2024 à 21:30
-- Version du serveur : 8.2.0
-- Version de PHP : 8.2.13

SET FOREIGN_KEY_CHECKS=0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `media`
--
CREATE DATABASE IF NOT EXISTS `media` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
USE media;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add emprunteur', 7, 'add_emprunteur'),
(26, 'Can change emprunteur', 7, 'change_emprunteur'),
(27, 'Can delete emprunteur', 7, 'delete_emprunteur'),
(28, 'Can view emprunteur', 7, 'view_emprunteur'),
(29, 'Can add jeu de plateau', 8, 'add_jeudeplateau'),
(30, 'Can change jeu de plateau', 8, 'change_jeudeplateau'),
(31, 'Can delete jeu de plateau', 8, 'delete_jeudeplateau'),
(32, 'Can view jeu de plateau', 8, 'view_jeudeplateau'),
(33, 'Can add dvd', 9, 'add_dvd'),
(34, 'Can change dvd', 9, 'change_dvd'),
(35, 'Can delete dvd', 9, 'delete_dvd'),
(36, 'Can view dvd', 9, 'view_dvd'),
(37, 'Can add cd', 10, 'add_cd'),
(38, 'Can change cd', 10, 'change_cd'),
(39, 'Can delete cd', 10, 'delete_cd'),
(40, 'Can view cd', 10, 'view_cd'),
(41, 'Can add livre', 11, 'add_livre'),
(42, 'Can change livre', 11, 'change_livre'),
(43, 'Can delete livre', 11, 'delete_livre'),
(44, 'Can view livre', 11, 'view_livre'),
(45, 'Can add membre', 7, 'add_membre'),
(46, 'Can change membre', 7, 'change_membre'),
(47, 'Can delete membre', 7, 'delete_membre'),
(48, 'Can view membre', 7, 'view_membre'),
(49, 'Can add emprunteur', 12, 'add_emprunteur'),
(50, 'Can change emprunteur', 12, 'change_emprunteur'),
(51, 'Can delete emprunteur', 12, 'delete_emprunteur'),
(52, 'Can view emprunteur', 12, 'view_emprunteur'),
(53, 'Can add emprunt cd', 13, 'add_empruntcd'),
(54, 'Can change emprunt cd', 13, 'change_empruntcd'),
(55, 'Can delete emprunt cd', 13, 'delete_empruntcd'),
(56, 'Can view emprunt cd', 13, 'view_empruntcd'),
(57, 'Can add emprunt dvd', 14, 'add_empruntdvd'),
(58, 'Can change emprunt dvd', 14, 'change_empruntdvd'),
(59, 'Can delete emprunt dvd', 14, 'delete_empruntdvd'),
(60, 'Can view emprunt dvd', 14, 'view_empruntdvd'),
(61, 'Can add emprunt livre', 15, 'add_empruntlivre'),
(62, 'Can change emprunt livre', 15, 'change_empruntlivre'),
(63, 'Can delete emprunt livre', 15, 'delete_empruntlivre'),
(64, 'Can view emprunt livre', 15, 'view_empruntlivre'),
(65, 'Can add cd', 16, 'add_cd'),
(66, 'Can change cd', 16, 'change_cd'),
(67, 'Can delete cd', 16, 'delete_cd'),
(68, 'Can view cd', 16, 'view_cd'),
(69, 'Can add dvd', 17, 'add_dvd'),
(70, 'Can change dvd', 17, 'change_dvd'),
(71, 'Can delete dvd', 17, 'delete_dvd'),
(72, 'Can view dvd', 17, 'view_dvd'),
(73, 'Can add emprunteur', 18, 'add_emprunteur'),
(74, 'Can change emprunteur', 18, 'change_emprunteur'),
(75, 'Can delete emprunteur', 18, 'delete_emprunteur'),
(76, 'Can view emprunteur', 18, 'view_emprunteur'),
(77, 'Can add jeu de plateau', 19, 'add_jeudeplateau'),
(78, 'Can change jeu de plateau', 19, 'change_jeudeplateau'),
(79, 'Can delete jeu de plateau', 19, 'delete_jeudeplateau'),
(80, 'Can view jeu de plateau', 19, 'view_jeudeplateau'),
(81, 'Can add emprunt dvd', 20, 'add_empruntdvd'),
(82, 'Can change emprunt dvd', 20, 'change_empruntdvd'),
(83, 'Can delete emprunt dvd', 20, 'delete_empruntdvd'),
(84, 'Can view emprunt dvd', 20, 'view_empruntdvd'),
(85, 'Can add emprunt cd', 21, 'add_empruntcd'),
(86, 'Can change emprunt cd', 21, 'change_empruntcd'),
(87, 'Can delete emprunt cd', 21, 'delete_empruntcd'),
(88, 'Can view emprunt cd', 21, 'view_empruntcd'),
(89, 'Can add emprunt livre', 22, 'add_empruntlivre'),
(90, 'Can change emprunt livre', 22, 'change_empruntlivre'),
(91, 'Can delete emprunt livre', 22, 'delete_empruntlivre'),
(92, 'Can view emprunt livre', 22, 'view_empruntlivre'),
(93, 'Can add livre', 23, 'add_livre'),
(94, 'Can change livre', 23, 'change_livre'),
(95, 'Can delete livre', 23, 'delete_livre'),
(96, 'Can view livre', 23, 'view_livre');

--
-- Déchargement des données de la table `bibliothecaire_app_cd`
--

INSERT INTO `bibliothecaire_app_cd` (`id`, `name`, `disponible`, `artiste`) VALUES
(1, 'L\'heure miroir', 0, 'Thibault Cauvin'),
(2, 'American Freedom Machine', 0, 'Harley Davidson');

--
-- Déchargement des données de la table `bibliothecaire_app_dvd`
--

INSERT INTO `bibliothecaire_app_dvd` (`id`, `name`, `disponible`, `realisateur`) VALUES
(1, 'Le Comte de Monte-Cristo', 0, 'Jacques Weber'),
(2, 'Le Seigneur des Anneaux', 1, 'Elijah Wood');

--
-- Déchargement des données de la table `bibliothecaire_app_empruntcd`
--

INSERT INTO `bibliothecaire_app_empruntcd` (`id`, `dateEmprunt`, `dateEmprunt_max`, `cd_id`, `membre_id`) VALUES
(1, '2024-07-20', '2024-07-27', 1, 1),
(2, '2024-07-20', '2024-07-27', 2, 2);

--
-- Déchargement des données de la table `bibliothecaire_app_empruntdvd`
--

INSERT INTO `bibliothecaire_app_empruntdvd` (`id`, `dateEmprunt`, `dateEmprunt_max`, `dvd_id`, `membre_id`) VALUES
(1, '2024-07-20', '2024-07-27', 1, 1);

--
-- Déchargement des données de la table `bibliothecaire_app_emprunteur`
--

INSERT INTO `bibliothecaire_app_emprunteur` (`id`, `name`, `NbEmprunt`, `bloque`) VALUES
(1, 'Jhon Doe', 2, 0),
(2, 'Will Smith', 1, 0);

--
-- Déchargement des données de la table `bibliothecaire_app_jeudeplateau`
--

INSERT INTO `bibliothecaire_app_jeudeplateau` (`id`, `name`, `createur`) VALUES
(1, 'Pandemic', 'Joshua Cappel'),
(2, 'Terraforming Mars', 'Isaac Fryxelius');

--
-- Déchargement des données de la table `bibliothecaire_app_livre`
--

INSERT INTO `bibliothecaire_app_livre` (`id`, `name`, `disponible`, `auteur`) VALUES
(1, 'Le petit prince', 1, 'Antoine de Saint-Exupéry'),
(2, 'Harry Potter', 1, 'J.K Rowling');

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mediatheque', 'membre'),
(8, 'mediatheque', 'jeudeplateau'),
(9, 'mediatheque', 'dvd'),
(10, 'mediatheque', 'cd'),
(11, 'mediatheque', 'livre'),
(12, 'mediatheque', 'emprunteur'),
(13, 'mediatheque', 'empruntcd'),
(14, 'mediatheque', 'empruntdvd'),
(15, 'mediatheque', 'empruntlivre'),
(16, 'bibliothecaire_app', 'cd'),
(17, 'bibliothecaire_app', 'dvd'),
(18, 'bibliothecaire_app', 'emprunteur'),
(19, 'bibliothecaire_app', 'jeudeplateau'),
(20, 'bibliothecaire_app', 'empruntdvd'),
(21, 'bibliothecaire_app', 'empruntcd'),
(22, 'bibliothecaire_app', 'empruntlivre'),
(23, 'bibliothecaire_app', 'livre');

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-07-11 16:36:18.460890'),
(2, 'auth', '0001_initial', '2024-07-11 16:36:19.017598'),
(3, 'admin', '0001_initial', '2024-07-11 16:36:19.182014'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-07-11 16:36:19.200338'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-07-11 16:36:19.211753'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-07-11 16:36:19.320676'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-07-11 16:36:19.404725'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-07-11 16:36:19.445376'),
(9, 'auth', '0004_alter_user_username_opts', '2024-07-11 16:36:19.457371'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-07-11 16:36:19.503209'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-07-11 16:36:19.503209'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-07-11 16:36:19.515634'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-07-11 16:36:19.560835'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-07-11 16:36:19.612215'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-07-11 16:36:19.650462'),
(16, 'auth', '0011_update_proxy_permissions', '2024-07-11 16:36:19.665760'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-07-11 16:36:19.700712'),
(18, 'mediatheque', '0001_initial', '2024-07-11 16:36:19.938046'),
(19, 'sessions', '0001_initial', '2024-07-11 16:36:19.972052'),
(20, 'mediatheque', '0002_rename_emprunteur_membre_rename_emprunteur_cd_membre_and_more', '2024-07-11 17:00:21.536209'),
(21, 'mediatheque', '0003_remove_cd_dateemprunt_remove_cd_membre_and_more', '2024-07-13 08:01:38.677761'),
(22, 'mediatheque', '0004_rename_nom_cd_name_rename_nom_dvd_name_and_more', '2024-07-13 08:20:02.806526'),
(23, 'mediatheque', '0005_alter_livre_membres', '2024-07-13 12:05:23.747428'),
(24, 'mediatheque', '0006_remove_cd_membres_remove_dvd_membres_and_more', '2024-07-13 12:12:26.248999'),
(25, 'mediatheque', '0007_membre_nbemprunt_empruntcd_cd_membres_empruntdvd_and_more', '2024-07-13 14:46:07.193662'),
(26, 'mediatheque', '0008_remove_empruntcd_dateremis_and_more', '2024-07-13 15:18:15.102623'),
(27, 'mediatheque', '0009_empruntcd_dateemprunt_max_empruntdvd_dateemprunt_max_and_more', '2024-07-14 10:28:35.775721'),
(28, 'mediatheque', '0010_alter_empruntcd_dateemprunt_and_more', '2024-07-14 20:26:08.748761'),
(29, 'bibliothecaire_app', '0001_initial', '2024-07-17 17:46:44.008766'),
(30, 'bibliothecaire_app', '0002_rename_emprunteur_membre_rename_emprunteur_cd_membre_and_more', '2024-07-17 17:46:44.228502'),
(31, 'bibliothecaire_app', '0003_remove_cd_dateemprunt_remove_cd_membre_and_more', '2024-07-17 17:46:44.538886'),
(32, 'bibliothecaire_app', '0004_rename_nom_cd_name_rename_nom_dvd_name_and_more', '2024-07-17 17:46:44.648469'),
(33, 'bibliothecaire_app', '0005_alter_livre_membres', '2024-07-17 17:46:44.648469'),
(34, 'bibliothecaire_app', '0006_remove_cd_membres_remove_dvd_membres_and_more', '2024-07-17 17:46:44.718652'),
(35, 'bibliothecaire_app', '0007_membre_nbemprunt_empruntcd_cd_membres_empruntdvd_and_more', '2024-07-17 17:46:45.030119'),
(36, 'bibliothecaire_app', '0008_remove_empruntcd_dateremis_and_more', '2024-07-17 17:46:45.109924'),
(37, 'bibliothecaire_app', '0009_empruntcd_dateemprunt_max_empruntdvd_dateemprunt_max_and_more', '2024-07-17 17:46:45.208933'),
(38, 'bibliothecaire_app', '0010_alter_empruntcd_dateemprunt_and_more', '2024-07-17 17:46:45.238692'),
(39, 'bibliothecaire_app', '0011_remove_cd_membres_remove_empruntcd_cd_and_more', '2024-07-17 17:46:45.461036'),
(40, 'bibliothecaire_app', '0012_initial', '2024-07-17 17:46:45.738907'),
(41, 'bibliothecaire_app', '0013_alter_empruntcd_dateemprunt_max_and_more', '2024-07-20 16:47:58.557779');
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
